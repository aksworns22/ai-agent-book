"""
实验 9-4 配套 demo：端到端语音思考 vs 级联流水线（真实跑通两条路并对照）。

书中实验 9-4 的核心是端到端语音思考模型 Step-Audio R1（直接「听→想→说」）。
Step-Audio R1 需多卡 GPU 部署、无公开 endpoint，本 demo 因此用 OpenAI 的
speech-to-speech 模型 `gpt-audio` 作为**真实可跑的端到端代表**（音频进、单模型、
音频出，无独立 ASR/LLM/TTS 三段），与**级联基线**（whisper-1 → gpt-4o-mini → tts-1）
同题对照，两条路的延迟都是真实测得、两段输出音频都用 ffprobe 校验。

流程：
  1. 用 TTS 合成一段「用户提问」的语音（一道需要多步推理的数学题，Spoken-MQA 风格），
     作为两条管道共同的输入；
  2. 端到端：一次 gpt-audio 调用，音频进 → 语音答案 + 转写出（单模型融合）；
  3. 级联：whisper-1 转写 → gpt-4o-mini 思考 → tts-1 合成回答语音（三段串行）；
  4. 打印两条路的真实延迟对照，并用 ffprobe 确认两段输出音频真实生成；
  5. 给出端到端 vs 级联的范式对照（延迟、副语言信息损失），并引用书中表 9-1。
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from speech_model import (
    CascadedSpeechModel,
    EndToEndSpeechModel,
    PipelineResult,
    synthesize_question_audio,
)

HERE = Path(__file__).parent
AUDIO_DIR = HERE / "audio"

# 一道需要多步推理的口述数学题（Spoken-MQA 风格：先听懂，再多步计算）
USER_QUESTION = (
    "小明有 12 块钱，他买了 3 支铅笔，每支 2 块钱，"
    "然后又用剩下的钱买了尽可能多的、每块 1 块 5 的橡皮，"
    "请问他最后还剩多少钱？"
)


def hr(char: str = "-", n: int = 68) -> str:
    return char * n


def ffprobe_info(audio_path: str) -> dict:
    """用 ffprobe 读取音频真实信息（时长、格式、码率），确认文件已生成。"""
    if not shutil.which("ffprobe"):
        return {"error": "未安装 ffprobe，跳过音频校验（brew install ffmpeg）"}
    try:
        out = subprocess.run(
            [
                "ffprobe", "-v", "error",
                "-show_entries", "format=duration,format_name,bit_rate,size",
                "-of", "json", audio_path,
            ],
            capture_output=True, text=True, check=True,
        )
        fmt = json.loads(out.stdout).get("format", {})
        return {
            "格式": fmt.get("format_name"),
            "时长(秒)": round(float(fmt.get("duration", 0)), 2),
            "码率(bps)": fmt.get("bit_rate"),
            "文件大小(字节)": fmt.get("size"),
        }
    except Exception as e:  # noqa: BLE001
        return {"error": f"ffprobe 失败：{e}"}


def print_e2e_result(result: PipelineResult, backend: str) -> None:
    s = result.stages[0]
    print(hr("="))
    print(f"范式一：端到端语音思考（后端={backend}，模型={s.model}）")
    print(hr("="))
    print("形态：音频进 → 单模型「听→想→说」→ 音频出（一次调用，无独立 ASR/LLM/TTS 段）")
    print(f"\n[单阶段] {s.name}  |  延迟={s.latency_s:.2f}s")
    if s.text is not None:
        print(f"    语音答案转写（模型顺带产出，非中间文本阶段）：{s.text}")
    print(f"    语音答案：{s.audio_path}")
    print(f"    ffprobe 校验：{ffprobe_info(s.audio_path)}")
    print(f"\n端到端总延迟（单模型一次前向）：{result.total_latency_s:.2f}s")


def print_cascade_result(result: PipelineResult) -> None:
    print("\n" + hr("="))
    print(f"范式二（对照基线）：级联流水线 ASR → LLM → TTS")
    print(hr("="))
    for i, s in enumerate(result.stages, 1):
        print(f"\n[阶段 {i}] {s.name}  |  模型={s.model}  |  延迟={s.latency_s:.2f}s")
        if s.text is not None:
            print(f"    文本：{s.text}")
        if s.audio_path is not None:
            print(f"    音频：{s.audio_path}")
            print(f"    ffprobe 校验：{ffprobe_info(s.audio_path)}")
    print(f"\n级联总延迟（各阶段串行相加）：{result.total_latency_s:.2f}s")


def print_comparison(e2e: PipelineResult, e2e_backend: str, cas: PipelineResult) -> None:
    """打印端到端 vs 级联的真实对照（实测延迟）+ 范式概念差异 + 书中表 9-1（引用）。"""
    stages = {s.name: s for s in cas.stages}
    asr = stages["ASR 语音识别"]
    llm = stages["LLM 思考"]
    tts = stages["TTS 语音合成"]

    print("\n" + hr("="))
    print("端到端 vs 级联：真实延迟对照")
    print(hr("="))
    print("\n【1】实测总延迟（本次运行，随网络与负载波动）")
    print(f"    端到端（{e2e_backend}，单模型一次调用）：{e2e.total_latency_s:.2f}s")
    print(f"    级联  ASR({asr.latency_s:.2f}s) + LLM({llm.latency_s:.2f}s) "
          f"+ TTS({tts.latency_s:.2f}s) = {cas.total_latency_s:.2f}s（三段串行累加）")
    delta = cas.total_latency_s - e2e.total_latency_s
    faster = "端到端更快" if delta > 0 else "级联更快"
    print(f"    差值：{abs(delta):.2f}s（{faster}）。注意端到端是「一次前向出整段音频」，"
          "真流式端到端还能「边想边说」把首字延迟进一步压低；级联的三段则天然串行累加。")

    print("\n【2】信息损失（副语言 / 语气）——范式差异，非本次延迟数字")
    print("    级联在 ASR 处把语音压成纯文本，说话人的情绪、语速、语调、重音、停顿，")
    print("    以及背景环境声/音乐在交接时几乎全部丢失——LLM 只看到「说了什么」，")
    print("    看不到「怎么说的」。本次输入语音在 ASR 处被抹平为纯文本：")
    print(f"        ASR 文本 → 「{asr.text}」")
    print("    端到端模型在隐空间（Latent Space）中直接传递这些副语言信息，能感知")
    print("    情绪/语速/语调，并据此生成有表现力、韵律匹配的回复。")

    print("\n【3】书中表 9-1：Step-Audio R1 不同语音思考配置（引自 Step-Audio R1 论文，"
          "非本 demo 产出）")
    print("    配置                          Spoken-MQA   URO-Bench")
    print("    不思考直接回答（基线）           70.6%        77.4")
    print("    MPS Speak-First（零延迟）        92.8%        82.5")
    print("    MPS Think-First（~80 tok 延迟）  93.9%        84.8")
    print("    完整 TBS（无延迟约束）           93.0%         —")
    print("    出处：Step-Audio R1 论文（书中表 9-1 转引）。这些是论文报告的评测分数，")
    print("    不是本 demo 跑出来的——本 demo 只产出上面【1】的真实延迟与两段真实音频。")
    print("    要点：Speak-First 几乎不损推理精度（92.8% ≈ TBS 93.0%），因为 CoT")
    print("    开头往往只是复述问题；这正是端到端「边想边说」能低延迟又不失准的原因。")

    print("\n【4】取舍小结")
    print("    级联：模块清晰、每段可独立调优、可解释性好；但延迟串行累加、副语言损失大。")
    print("    端到端：延迟更低、保留非文字信息、韵律自然；代价是训练数据需求大、")
    print("            可解释性差。二者在 2026 年的生产系统中长期并存。")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="实验 9-4：端到端语音思考 vs 级联流水线。合成一段「用户提问」语音，"
                    "同题跑通端到端（gpt-audio，可切 Step-Audio R1）与级联"
                    "（whisper-1 → gpt-4o-mini → tts-1），打印真实延迟对照。",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--question", default=USER_QUESTION,
                   help="自定义口述提问（默认为一道 Spoken-MQA 风格的多步数学题）。")
    p.add_argument("--skip-cascade", action="store_true",
                   help="只跑端到端，不跑级联对照基线。")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    question = args.question

    load_dotenv(HERE / ".env")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("错误：未配置 OPENAI_API_KEY。请复制 env.example 为 .env 并填入有效的 "
              "OpenAI Key。", file=sys.stderr)
        return 1

    # timeout + 自动重试：单次网络/SSL 抖动不至于让整条流水线崩溃
    client = OpenAI(api_key=api_key, timeout=120.0, max_retries=3)
    AUDIO_DIR.mkdir(exist_ok=True)
    question_audio = str(AUDIO_DIR / "user_question.mp3")
    e2e_audio = str(AUDIO_DIR / "answer_end_to_end.wav")
    cascade_audio = str(AUDIO_DIR / "answer_cascade.mp3")

    # -- 步骤 1：合成「用户提问」语音（两条管道共同输入） ----------------------
    print(hr("="))
    print("步骤 1：用 TTS 合成一段「用户提问」语音（作为两条管道共同的输入）")
    print(hr("="))
    print(f"提问文本：{question}")
    synthesize_question_audio(client, question, question_audio)
    print(f"已生成输入音频：{question_audio}")
    print(f"ffprobe 校验：{ffprobe_info(question_audio)}")

    # -- 步骤 2：端到端语音思考（真实跑通） -----------------------------------
    print("\n" + hr("="))
    print("步骤 2：端到端语音思考（音频进 → 单模型 → 音频出）")
    print(hr("="))
    e2e_model = EndToEndSpeechModel(client)
    backend = e2e_model.backend
    if backend == "step-audio-r1":
        print(f"检测到 STEP_AUDIO_ENDPOINT={e2e_model.endpoint}，走真实 Step-Audio R1。")
    else:
        print(f"未配置 STEP_AUDIO_ENDPOINT，用 OpenAI speech-to-speech 模型 "
              f"{e2e_model.model} 作为端到端代表（真正的音频→单模型→音频）。")
        print("如需换成书中的 Step-Audio R1，自部署后把地址写入 STEP_AUDIO_ENDPOINT 即可。\n")
    try:
        e2e_result = e2e_model.run(question_audio, e2e_audio)
    except Exception as e:  # noqa: BLE001
        print(f"错误：端到端调用失败：{e}", file=sys.stderr)
        return 2
    print_e2e_result(e2e_result, backend)

    # -- 步骤 3：级联流水线（对照基线） ---------------------------------------
    cascade_result = None
    if not args.skip_cascade:
        cascaded = CascadedSpeechModel(client)
        cascade_result = cascaded.run(question_audio, cascade_audio)
        print_cascade_result(cascade_result)

    # -- 步骤 4：真实延迟对照 + 范式差异 + 表 9-1（引用） ---------------------
    if cascade_result is not None:
        print_comparison(e2e_result, backend, cascade_result)

    print("\n完成。可试听：")
    print(f"  ffplay {e2e_audio}      # 端到端语音答案")
    if cascade_result is not None:
        print(f"  ffplay {cascade_audio}   # 级联语音答案")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
