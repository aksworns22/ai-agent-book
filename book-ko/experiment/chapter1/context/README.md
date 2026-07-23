# 제거 실험을 지원하는 컨텍스트 인식 AI Agent

여러 LLM 공급자(SiliconFlow Qwen, ByteDance Doubao, Moonshot Kimi)를 지원하는 고급 AI Agent 구현이다. 체계적인 제거 실험을 통해 컨텍스트 구성 요소가 얼마나 중요한지 보여 주기 위해 설계되었다.

## 🎯 개요

이 프로젝트는 여러 도구(PDF 파싱, 통화 환산, 계산기, 코드 인터프리터)를 사용하는 컨텍스트 인식 AI Agent를 구현하고, 다양한 컨텍스트 구성 요소가 Agent의 행동과 성능에 어떤 영향을 미치는지 탐구할 수 있는 종합적인 제거 실험 기능을 제공한다.

### 주요 기능

- **다중 공급자 지원**: SiliconFlow(Qwen), Doubao(ByteDance), Kimi(Moonshot) LLM 지원
- **다중 도구 Agent**: PDF 파싱, 통화 환산, 계산, Python 코드 실행
- **컨텍스트 모드**: 제거 실험을 위한 다섯 가지 컨텍스트 구성
- **대화형 및 일괄 처리 모드**: 단일 작업 또는 종합 테스트 스위트 실행
- **대화 기록**: 한 세션의 여러 질의에 걸쳐 컨텍스트 유지
- **상세 분석**: 성능 지표, 시각화, 종합 보고서 제공

## 🤖 지원하는 LLM 공급자

### Doubao(ByteDance) - 기본값
- **모델**: doubao-seed-1-6-thinking-250715(변경 가능)
- **API**: Volcano Engine을 통한 OpenAI 호환 API
- **적합한 작업**: 고급 추론, 빠른 응답, 영어 및 중국어 작업

### SiliconFlow
- **모델**: Qwen/Qwen3.5-397B-A17B(변경 가능)
- **API**: OpenAI 호환 API
- **적합한 작업**: 복잡한 추론 작업, 상세 분석

### Kimi(Moonshot AI)
- **모델**: kimi-k3(K3 추론 모델, temperature는 1로 고정되며 max_tokens는 사고 출력을 수용할 수 있을 만큼 크게 설정됨)
- **API**: Moonshot 플랫폼을 통한 OpenAI 호환 API
- **적합한 작업**: 고급 추론, 다중 턴 대화, 영어 및 중국어 작업
- **기능**: 비용 최적화를 위한 컨텍스트 캐싱

## 🏗️ 아키텍처

### 컨텍스트 구성 요소

1. **전체 컨텍스트** - 모든 구성 요소를 갖춘 완전한 Agent
2. **과거 메시지 없음** - 과거 도구 호출 추적 제외
3. **사고 과정 없음** - 전략적 계획 없이 동작
4. **도구 호출 없음** - 외부 도구 실행 불가
5. **도구 실행 결과 없음** - 도구 실행 결과를 볼 수 없음

### 사용 가능한 도구

- **`parse_pdf(url)`** - PDF 문서를 다운로드하고 텍스트 추출
- **`convert_currency(amount, from, to)`** - 실시간 통화 환산
- **`calculate(expression)`** - 간단한 수식 계산
- **`code_interpreter(code)`** - 복잡한 계산, 합계 산출, 데이터 처리를 위한 Python 코드 실행

## 📋 사전 요구 사항

- Python 3.8 이상
- 지원하는 공급자 중 하나의 API 키:
  - **SiliconFlow**: [SiliconFlow](https://siliconflow.cn)에서 발급
  - **Doubao(ByteDance)**: [Volcano Engine](https://www.volcengine.com/)에서 발급
  - **Kimi(Moonshot)**: [Moonshot Platform](https://platform.moonshot.cn/)에서 발급

## 📝 예제 작업

시스템에는 서로 다른 역량을 보여 주는 사전 정의된 예제 작업 다섯 개가 포함되어 있다.

1. **간단한 통화 환산** - 기본적인 다중 통화 계산
2. **다중 통화 예산 분석** - 여러 사무실의 복잡한 비용 분석
3. **PDF 재무 분석** - 재무 문서 파싱 및 분석
4. **투자 성장 계산** - 통화 환산을 포함한 복리 계산
5. **종합 재무 보고서** - 모든 도구를 사용하는 전체 워크플로

이 예제들은 Agent의 역량과 컨텍스트 제거가 미치는 영향을 보여 주도록 설계되었다.

## 🚀 빠른 시작

### 1. 설치

```bash
# 저장소 복제
cd projects/week1/context

# 의존성 설치
pip install -r requirements.txt

# 환경 설정 파일 복사 및 구성
cp env.example .env
# .env를 편집하고 API 키(SILICONFLOW_API_KEY 또는 ARK_API_KEY) 추가
```

### 2. 공급자 설정

```bash
# Doubao(ByteDance) - 기본값
export ARK_API_KEY=your_key_here
python main.py  # 기본적으로 Doubao 사용

# SiliconFlow(Qwen)
export SILICONFLOW_API_KEY=your_key_here
python main.py --provider siliconflow

# Kimi(Moonshot)
export MOONSHOT_API_KEY=your_key_here
python main.py --provider kimi

# 또는 사용자 지정 모델 지정
python main.py --model doubao-seed-1-6-thinking-250715

# 범용 OpenRouter 폴백: 위 공급자의 키가 없거나 유효하지 않지만
# OPENROUTER_API_KEY가 설정되어 있으면 요청을 OpenRouter로 라우팅하고
# 모델 ID를 자동 매핑한다(bare gpt-*/o1-* -> openai/*, claude-* ->
# anthropic/*, 그 밖의 네이티브 ID -> OPENROUTER_MODEL 또는 openai/gpt-5.6-luna).
export OPENROUTER_API_KEY=sk-or-v1-your-key-here
python main.py                       # ARK_API_KEY가 없으면 OpenRouter로 폴백
python main.py --provider openrouter # 또는 OpenRouter를 직접 사용
```

### 3. Kimi 연동 테스트

```bash
# Kimi K3 모델 빠른 테스트
export MOONSHOT_API_KEY=your_key_here
python test_kimi.py

# 메인 스크립트에서 Kimi 사용
python main.py --provider kimi --mode interactive

# Kimi로 제거 실험 실행
python main.py --provider kimi --mode ablation
```

### 4. 대화형 모드 실행(권장)

```bash
# 기본값(Doubao)
python main.py --mode interactive

# SiliconFlow 공급자 사용
python main.py --mode interactive --provider siliconflow

# 대화형 모드에서 사용할 수 있는 명령:
# - 'samples': 사전 정의된 작업 보기
# - 'sample 3': PDF 파싱 테스트
# - 'providers': 사용 가능한 공급자 목록 보기
# - 'provider kimi': 공급자 전환
# - 'status': 현재 설정 보기
# - 'help': 모든 명령 보기
```

### 5. 예제 작업 실행

```bash
# 인수 없이 실행하여 예제 중 하나 선택
python main.py --mode single

# 특정 공급자 사용
python main.py --mode single --provider doubao

# 또는 직접 작성한 작업 전달
python main.py --mode single \
  --task "미화 1,000달러를 EUR, GBP, JPY로 환산하고 평균을 계산하세요." \
  --context-mode full \
  --provider siliconflow
```

### 6. 제거 실험 실행

```bash
# 기본 공급자 사용(단일 사례, 컨텍스트 모드 다섯 개 모두)
python main.py --mode ablation

# Doubao 공급자 사용
python main.py --mode ablation --provider doubao

# 여러 사례를 모든 모드에서 비교(책의 주장을 뒷받침하는 더 강한 증거)
python main.py --mode ablation --cases 3

# 두 모드만 비교하고 원시 결과를 사용자 지정 경로에 저장
python main.py --mode ablation --ablation-modes full no_history --output my_ablation.json
```

`main.py`는 유일한 CLI 진입점이다. 전체 중국어 옵션 설명은 `python main.py --help`로 확인할 수 있다.

주요 옵션:

| 옵션 | 설명 |
|------|------|
| `--mode` | `single` / `ablation` / `interactive`(기본값) |
| `--task` | `single` 모드에서 실행할 작업 텍스트 |
| `--context-mode` | `single` 모드의 컨텍스트 모드(`full`, `no_history`, `no_reasoning`, `no_tool_calls`, `no_tool_results`) |
| `--ablation-modes` | `ablation` 모드에서 테스트할 모드의 일부 또는 전부(기본값: 다섯 개 모두) |
| `--cases` | `ablation` 모드에서 각 모드로 실행할 사례 수(기본값: 1) |
| `--provider` / `--model` | LLM 공급자 및 선택적인 모델 재정의 |
| `--output` | JSON 결과(`single`) 또는 원시 결과(`ablation`)의 출력 경로 |

## 🧪 제거 실험

제거 실험은 컨텍스트 구성 요소를 체계적으로 제거하여 각 요소의 중요성을 파악한다.

### 테스트 시나리오

다음 작업이 필요한 복잡한 재무 분석 작업을 사용한다.
1. PDF 문서 파싱
2. 여러 통화 환산
3. 수학 계산
4. 결과 집계

### 예상 동작

| 컨텍스트 모드 | 제거한 구성 요소(책 §실험 1-1) | 예상 동작 | 영향 |
|-------------|-----------------------------------|-------------------|---------|
| **full** | 없음(기준선) | 전체 작업을 성공적으로 실행 | 기준 성능 |
| **no_history** | 과거 메시지(history) | 중복 작업과 비효율 발생 | 도구 호출을 반복할 수 있음 |
| **no_reasoning** | 사고 과정(reasoning) | 체계적이지 않은 접근, 오류 가능성 | 전략적 계획 부족 |
| **no_tool_calls** | 도구 정의(tool definitions) | 완전한 실패 | 외부 세계와 상호작용할 수 없음 |
| **no_tool_results** | 도구 실행 결과(tool results) | 잘못된 결론 | 피드백 없이 의사결정 |

**각 제거 실험의 적용 방식**(`agent.py` 참고):

- **no_tool_calls** - 요청에서 `tools` 파라미터를 생략하므로 모델이 호출할 수 있는 도구 정의가 없다.
- **no_tool_results** - 모든 도구 실행 결과를 `[Tool result hidden]` 자리표시자로 바꾼다.
- **no_reasoning** - 각 모델 응답을 궤적에 다시 추가하기 전에 `reasoning_content`를 제거한다.
- **no_history** - `_prepare_messages_for_api()`가 모델에 슬라이딩 윈도(시스템 프롬프트 + 현재 작업 + 가장 최근의 ReAct 단계)만 전송한다. 따라서 이전 단계를 잊은 Agent가 도구 호출을 반복하는 경향이 있다. 전체 모드는 항상 완전한 궤적을 전송한다.

### 테스트 실행

```bash
# 전체 제거 실험 실행(단일 사례, 모드 다섯 개 모두)
python main.py --mode ablation

# 더 강한 비교를 위해 여러 사례로 실행
python main.py --mode ablation --cases 3

# 생성되는 파일:
# - ablation_study_results.png(시각화, matplotlib가 설치된 경우)
# - ablation_study_report.md(상세 보고서)
# - ablation_results.json(원시 데이터, --output으로 경로 재정의 가능)
```

콘솔에는 실행별 **제거 실험 결과** 표와 각 구성 요소의 영향을 한눈에 볼 수 있는 **비교 행렬**(컨텍스트 모드 x 사례)이 출력된다.

## 📊 결과 이해하기

### 성능 지표

- **성공률**: 작업을 올바르게 완료했는지 여부
- **실행 시간**: 작업을 완료하는 데 걸린 총시간
- **반복 횟수**: Agent와 모델 간 상호작용 횟수
- **도구 호출**: 외부 도구를 호출한 횟수
- **사고 단계**: 전략적 계획을 수행한 횟수

### 출력 예시

```
제거 실험 결과
================================================================================
| 테스트 이름                    | 성공    | 시간   | 반복 횟수 | 도구 호출 |
|--------------------------------|---------|--------|-----------|-----------|
| 기준선 - 전체 컨텍스트         | ✓       | 12.3s  | 5         | 8         |
| 과거 도구 호출 없음            | ✓       | 18.7s  | 8         | 12        |
| 사고 과정 없음                 | ✗       | 25.4s  | 10        | 15        |
| 도구 호출 명령 없음            | ✗       | 3.2s   | 2         | 0         |
| 도구 호출 결과 없음            | ✗       | 15.6s  | 10        | 10        |
```

## 💡 핵심 통찰

### 1. 도구 호출은 기본 요소다
도구 호출 기능이 없으면 Agent는 외부 시스템과 상호작용할 수 없으므로 작업을 완료할 수 없다.

### 2. 도구 실행 결과는 핵심 피드백을 제공한다
결과를 볼 수 없으면 Agent는 눈먼 상태로 동작해 잘못된 결론을 내리고 무한 루프에 빠진다.

### 3. 사고 과정은 효율을 높인다
전략적 계획은 반복 횟수와 도구 호출 횟수를 줄여 속도와 정확도를 모두 높인다.

### 4. 과거 메시지는 중복을 방지한다
과거 컨텍스트는 작업 반복을 방지하고 여러 반복 단계에 걸쳐 작업의 일관성을 유지한다.

## 🛠️ 고급 사용법

### 대화형 모드 명령

대화형 모드는 다음 명령을 지원한다.

| 명령 | 설명 |
|---------|-------------|
| `samples` | 사용 가능한 모든 예제 작업 표시 |
| `sample <n>` | n번째 예제 작업 실행 |
| `providers` | 사용 가능한 모든 LLM 공급자 나열 |
| `provider <name>` | 다른 공급자로 전환(예: `provider kimi`) |
| `modes` | 제거 실험에서 사용 가능한 컨텍스트 모드 나열 |
| `mode <name>` | 컨텍스트 모드 전환(예: `mode no_history`) |
| `status` | 현재 설정(공급자, 모델, 모드 등) 표시 |
| `reset` | Agent 궤적 초기화(기록 삭제) |
| `create_pdfs` | 테스트용 예제 PDF 파일 생성 |
| `quit` | 대화형 모드 종료 |

**참고:** 프롬프트는 `[KIMI]>` 또는 `[DOUBAO]>`와 같이 현재 공급자를 대괄호 안에 표시한다.

### 대화 기록

Agent는 대화형 세션 내내 대화 기록을 유지한다.

- **지속적인 컨텍스트**: 한 세션 안에서 이전 질의와 응답을 기억
- **다중 턴 대화**: 대화 앞부분의 정보를 참조 가능
- **도구 호출 기억**: 이전 도구 실행을 기억하고 참조 가능
- **요청 시 초기화**: `reset` 명령으로 기록을 삭제하고 새로 시작

대화 흐름 예시:
```
[DOUBAO]> 예산이 10,000달러라는 것을 기억하세요. 그중 15%를 계산하세요.
# Agent가 계산한 뒤 예산을 기억함

[DOUBAO]> 이제 그 15%에 해당하는 금액을 EUR로 환산하세요.
# Agent가 다시 묻지 않고 앞서 계산한 금액을 사용함

[DOUBAO]> 원래 예산이 얼마였나요?
# Agent가 앞에서 언급한 10,000달러를 기억해 냄
```

### 사용자 지정 작업

직접 테스트 시나리오를 작성할 수 있다.

```python
from agent import ContextAwareAgent, ContextMode

agent = ContextAwareAgent(api_key, ContextMode.FULL)
result = agent.execute_task("""
    https://example.com/report.pdf에서 PDF를 다운로드하고
    모든 금액을 추출해 EUR로 환산한 뒤
    합계를 계산하세요.
""")
```

### 테스트 PDF 생성

테스트에 사용할 예제 PDF를 생성한다.

```bash
python create_sample_pdf.py
# 재무 보고서 예제가 담긴 test_pdfs/ 디렉터리 생성
```

### 설정

`config.py`를 편집하거나 환경 변수를 설정한다.

```bash
export MODEL_TEMPERATURE=0.5
export MAX_ITERATIONS=15
export LOG_LEVEL=DEBUG
```

## 📁 프로젝트 구조

```
context/
├── agent.py              # Agent 핵심 구현 + 컨텍스트 모드
├── main.py               # 단일 CLI 진입점(single / ablation / interactive)
├── config.py             # 설정 관리
├── create_sample_pdf.py # PDF 생성 유틸리티
├── requirements.txt     # 의존성
├── env.example         # 환경 설정 템플릿
└── README.md           # 이 문서
```

> 참고: 제거 실험은 `main.py`의 `AblationTestSuite`에 있으며
> `python main.py --mode ablation`으로 실행한다. 별도의 `ablation_tests.py`는 없다.

## 🔬 연구 활용 분야

이 구현은 다음 분야에 유용하다.

- **AI 안전 연구**: 실패 양상 이해
- **시스템 설계**: 핵심 구성 요소 식별
- **최적화**: 실행 가능한 최소 구성 탐색
- **교육**: Agent 아키텍처 원리 교육

## 🤝 기여하기

기여를 환영한다. 다음 영역을 개선할 수 있다.

- 도구 구현 추가
- 더 정교한 테스트 시나리오
- 다른 컨텍스트 제거 전략
- 성능 최적화

## ⚠️ 한계

- 환율이 고정되어 있음(프로덕션 환경에서는 실시간 API를 사용해야 함)
- 복잡한 레이아웃의 PDF는 파싱에 실패할 수 있음
- 문서가 매우 크면 모델의 토큰 제한에 영향을 받을 수 있음

## 📝 라이선스

MIT 라이선스 - 자세한 내용은 LICENSE 파일 참고

## 🙏 감사의 말

- Qwen 모델 API를 제공한 SiliconFlow
- 클라이언트 라이브러리를 제공한 OpenAI
- AI Agent 연구 커뮤니티

## 📧 문의

질문이나 의견이 있으면 GitHub에서 이슈를 열어 달라.

---

**참고**: 이 프로젝트는 AI Agent의 제거 실험을 보여 주는 교육용 프로젝트다. 프로덕션 환경에서 사용하려면 적절한 오류 처리, 속도 제한, 보안 조치를 구현해야 한다.
