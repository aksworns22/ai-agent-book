# AI Agent 심층 이해: 설계 원리와 엔지니어링 실전

**[English](README.en.md) | 한국어 | [中文](book/) | [Tiếng Việt](README.vi.md) | [தமிழ்](README.ta.md)**

이 저장소는 《AI Agent 심층 이해: 설계 원리와 엔지니어링 실전》의 오픈 소스 메인 저장소로, **책의 전체 본문**과 **실습 예제 코드**를 담고 있습니다. 전체 본문과 삽화, 실험 코드는 모두 오픈 소스로 공개되어 있습니다. 직접 실험을 실행해 보고 Issue와 PR을 제출해 주세요.

## 📖 전자책

이 책은 여러 언어로 제공됩니다.

- **중국어 PDF(원문 / 中文原版)**: [`book/深入理解-AI-Agent-李博杰-v1.2.pdf`](book/深入理解-AI-Agent-李博杰-v1.2.pdf)
- **영어 PDF**([@nsdevaraj](https://github.com/nsdevaraj)의 커뮤니티 번역): [`book-en/AI-Agents-in-Depth-Bojie-Li-v1.2.pdf`](book-en/AI-Agents-in-Depth-Bojie-Li-v1.2.pdf)
- **타밀어 PDF**([@nsdevaraj](https://github.com/nsdevaraj)의 커뮤니티 번역): [`book-ta/AI-Agents-in-Depth-Bojie-Li-v1.2-ta.pdf`](book-ta/AI-Agents-in-Depth-Bojie-Li-v1.2-ta.pdf)
- **베트남어 PDF**([@toanalien](https://github.com/toanalien)의 커뮤니티 번역): [`book-vi/AI-Agents-in-Depth-Bojie-Li-v1.1-vi.pdf`](book-vi/AI-Agents-in-Depth-Bojie-Li-v1.1-vi.pdf)

중국어 원문은 [`book/`](book/)에 있습니다. 영어·타밀어·베트남어 번역은 **커뮤니티에서 기여**했으며 각각 [`book-en/`](book-en/), [`book-ta/`](book-ta/), [`book-vi/`](book-vi/)에 있습니다. 이 번역들은 중국어 원문보다 업데이트가 늦을 수 있습니다.

- **영어 원고**: `book-en/introduction.md`(서문), `book-en/chapter1.md` ~ `book-en/chapter10.md`(1~10장), `book-en/afterword.md`(후기)
- **직접 빌드**: pandoc, xelatex, ElegantBook 문서 클래스와 관련 글꼴을 설치한 뒤 다음 명령을 실행합니다.

  ```bash
  cd book-en && bash build_pdf.sh
  ```

  그림은 `book-en/gen_*_figs.py`로 생성되어 `book-en/images/`에 저장됩니다. 조판 관련 세부 설정은 `book-en/preamble.tex`과 `book-en/*.lua`에서 확인할 수 있습니다.

## 📑 내용 개요(1~10장)

이 책은 **Agent = LLM + 컨텍스트 + 도구**라는 핵심 공식을 중심으로 다음 열 개 장을 전개합니다.

- **1장 · Agent 기초**: “모델이 곧 Agent”라는 새로운 패러다임에서 출발해 **Agent = LLM + 컨텍스트 + 도구**라는 핵심 공식을 세우고, 모델 외부의 모든 엔지니어링 역량이 진정한 경쟁력이라는 Harness 엔지니어링을 소개합니다.
- **2장 · 컨텍스트 엔지니어링**: 컨텍스트는 Agent 역량의 상한을 결정합니다. LLM API의 컨텍스트 구조, KV Cache 친화적 설계, 프롬프트 엔지니어링, 동적 프롬프트와 Agent Skills, 상태 표시줄 메타 정보, 컨텍스트 압축 전략을 깊이 살펴봅니다.
- **3장 · 사용자 메모리와 지식 베이스**: Agent가 세션을 넘어 사용자를 기억하고 외부 지식에 접근하도록 합니다. 사용자 메모리 시스템, 기본 RAG 파이프라인, 평면 텍스트를 넘어선 지식 구성과 검색(구조화 인덱스, 지식 그래프 등)을 다룹니다.
- **4장 · 도구**: 도구는 Agent의 손입니다. 도구 분류와 일반 설계 원칙, MCP 프로토콜과 도구 선택의 난제, 세 가지 도구 유형(인식·실행·협업), 이벤트 기반 비동기 Agent를 설명합니다.
- **5장 · Coding Agent와 코드 생성**: 코드는 “새로운 도구를 만들 수 있는 도구”이자 범용 Agent의 메타 역량입니다. 프로덕션급 Coding Agent를 예로 들어 가장 강력한 범용 도구의 완전한 구현을 보여 줍니다.
- **6장 · Agent 평가**: Agent 성능을 비교 가능한 신호로 바꿉니다. 평가 환경, 데이터셋 설계, 지표 체계, 통계적 유의성, 관측 가능성, 평가 기반 선택, 프로덕션급 내부 평가 및 시뮬레이션 환경을 다룹니다.
- **7장 · 모델 사후 학습**: 사전 학습, SFT, RL의 세 단계를 종합적으로 살펴봅니다. SFT와 RL의 선택 기준, RLHF, 알고리즘 비교, 데이터와 환경, 모델에 도구 호출을 가르치고 샘플 효율을 높이는 최신 연구를 다룹니다.
- **8장 · Agent 자기 진화**: 가중치를 바꾸지 않고 성장합니다. 세 가지 학습 패러다임, 경험으로부터의 학습, 능동적 도구 발견, “도구 사용자”에서 “도구 제작자”로 가는 과정을 통해 Agent가 “똑똑한” 상태에서 “숙련된” 상태로 발전하게 합니다.
- **9장 · 멀티모달과 실시간 상호작용**: 인식과 행동을 텍스트에서 음성, GUI, 물리 세계로 확장합니다. 세 가지 음성 패러다임(캐스케이드형/종단 간 풀 모달/전이중), 스트리밍 음성 인식과 합성, Computer Use, 로봇 조작을 다룹니다.
- **10장 · 다중 Agent 협업**: 집단 지능은 개별 지능을 넘어설 수 있습니다. 다중 Agent 분류 체계, 단일 Agent보다 실제로 우수한 경우, 컨텍스트 공유 여부에 따른 협업, 실패 유형, 새롭게 등장하는 “Agent 사회”를 다룹니다.

## 💻 실습 코드

모든 프로젝트는 책의 열 개 장과 일대일로 대응하도록 **장별**로 구성되어 있으며, `chapterN/project_name/` 디렉터리에서 기본 개념부터 고급 기법까지 완전한 학습 경로를 제공합니다. 현재 5·8·9·10장의 실험 대부분은 실제 LLM API로 검증한 독립 실행형 데모를 제공합니다.

### 프로젝트 유형 설명

실습 프로젝트는 세 가지 유형으로 나뉩니다. 아래 아이콘을 통해 각 프로젝트를 얼마나 바로 실행할 수 있는지 확인하세요.

- ✅ **독립 실행 가능**: 이 저장소에 전체 코드가 들어 있습니다. API 키만 설정하면(문서 끝부분 참고) 실행할 수 있습니다.
- 📖 **재현 가이드**: 프로젝트 자체가 상세한 재현 문서입니다. 별도로 `git clone`해야 하는 **외부 저장소**(학습 프레임워크, 평가 벤치마크 등)에 의존합니다. 아래 *외부 저장소 가져오기*를 참고하세요.
- 🚧 **설계 문서**: 현재는 아키텍처와 구현 계획 문서만 포함되어 있으며, 실행 가능한 코드는 아직 개선 중입니다.

다음 프로젝트는 ✅ 독립 실행형이 아니므로 저장소를 복제할 때 참고하세요.

| 프로젝트 | 유형 | 설명 |
| --- | --- | --- |
| `chapter7/AdaptThink` · `AWorld-train` · `MiniMind-pretrain` · `retool` · `SpatialReasoning` | 📖 재현 가이드 | 외부 프레임워크에 의존하는 학습 실험입니다. README에 따라 재현하세요. |
| 6장의 모든 벤치마크 · 7장의 학습 프레임워크 대부분 · 9장의 `browser-use`/`claude-quickstarts` · 10장의 `use-computer-while-calling` | 📖 재현 가이드 | 외부 저장소에 의존합니다. *외부 저장소 가져오기*를 참고하세요. |

### 외부 저장소 가져오기(요약)

6·7·9·10장의 **일부** 실험은 평가 벤치마크, 학습 프레임워크, 로봇 플랫폼 같은 **외부 저장소**에 의존합니다. 크기와 라이선스 문제로 이 저장소에는 포함되어 있지 않습니다. 처음부터 정보가 너무 많아지는 일을 피하고자, **전체 clone 명령과 업스트림 주소, 책에서 검증한 커밋을 이 문서 끝의 *부록 · 외부 저장소 가져오기*에 정리했습니다.** 먼저 앞 장의 독립 실행형 프로젝트로 시작하고, 학습·평가·로봇 실험을 재현할 때 문서 끝의 안내에 따라 필요한 리소스를 받는 것을 권장합니다.

## 🚀 1장 · Agent 기초

### learning-from-experience - 강화 학습과 LLM 비교
`chapter1/learning-from-experience/`

전통적인 강화 학습(Q-learning)과 LLM 기반 인컨텍스트 학습을 비교하여 Shunyu Yao의 “The Second Half” 블로그 글에서 제시한 핵심 통찰을 재현합니다. 보물찾기 게임을 통해 LLM이 전통적인 RL보다 250~400배 높은 샘플 효율로 더 나은 성능을 낼 수 있음을 보여 줍니다.

**핵심 개념**: 강화 학습, 인컨텍스트 학습, 샘플 효율, 사전 지식

### web-search-agent - Agent로서의 Kimi K2 모델
`chapter1/web-search-agent/`

여러 차례 검색하고 정보를 통합할 수 있는 기본적인 심층 검색 Agent를 구현합니다.

**핵심 개념**: 웹 검색, 모델 네이티브 Agent

### search-codegen - GPT-5 네이티브 도구 통합
`chapter1/search-codegen/`

웹 검색과 코드 실행 등의 도구를 이용해 복잡한 분석을 수행하는 기본 심층 검색 및 코드 샌드박스 Agent를 구축합니다.

**핵심 개념**: 웹 검색, 코드 생성, 모델 네이티브 Agent

### context - 컨텍스트 어블레이션 연구
`chapter1/context/`

체계적인 어블레이션 실험을 통해 여러 Agent 컨텍스트 구성 요소의 중요성을 보여 줍니다. 여러 LLM 공급자(SiliconFlow Qwen, ByteDance Doubao, Moonshot Kimi)를 지원하며, 서로 다른 컨텍스트 모드를 설정해 Agent 행동의 변화를 관찰할 수 있습니다.

**핵심 개념**: 컨텍스트 관리, 도구 호출, ReAct 루프, 어블레이션 연구

## 🎯 2장 · 컨텍스트 엔지니어링

### local_llm_serving - 로컬 LLM 배포와 도구 호출
`chapter2/local_llm_serving/`

최적의 백엔드(vLLM 또는 Ollama)를 자동으로 선택하는 크로스 플랫폼 로컬 LLM 배포 솔루션입니다. 뛰어난 시스템 설계를 통해 0.6B 소형 모델도 훌륭한 도구 호출 역량을 발휘할 수 있음을 보여 줍니다. 사고 과정을 실시간으로 표시할 수 있도록 스트리밍 응답을 지원합니다.

**핵심 개념**: 모델 배포, 채팅 템플릿, 스트리밍, 도구 호출

### attention_visualization - 어텐션 메커니즘 시각화
`chapter2/attention_visualization/`

LLM의 전체 입출력 토큰 시퀀스와 어텐션 가중치 분포를 시각화하여 모델이 컨텍스트를 처리하고 추론하며 도구를 호출하는 방식을 깊이 이해할 수 있게 합니다.

**핵심 개념**: 어텐션 메커니즘, 토큰 분석, 추론 과정 시각화

### kv-cache - KV Cache 친화적 컨텍스트 설계
`chapter2/kv-cache/`

서로 다른 컨텍스트 관리 방식이 KV Cache에 미치는 영향을 살펴보고, 흔한 오류 패턴이 캐시 효율을 어떻게 무너뜨리는지 보여 줍니다. 올바른 컨텍스트 설계로 지연 시간과 비용을 크게 줄일 수 있음을 실험으로 확인합니다.

**핵심 개념**: KV Cache, 컨텍스트 최적화, 성능 튜닝

### context-compression - 컨텍스트 압축 전략
`chapter2/context-compression/`

요약, 핵심 정보 추출, 의미 압축을 비롯한 여러 컨텍스트 압축 전략을 구현하고 비교합니다. Agent 역량을 유지하면서 토큰 사용량을 줄입니다.

**핵심 개념**: 컨텍스트 압축, 토큰 최적화, 정보 밀도

### prompt-engineering - 프롬프트 엔지니어링 어블레이션 연구
`chapter2/prompt-engineering/`

Tau-Bench 프레임워크를 확장하여 체계적인 어블레이션 실험으로 여러 프롬프트 엔지니어링 요소가 Agent 성능에 미치는 영향을 정량화합니다. 어조, 지시 구성, 도구 설명 같은 요소가 작업 완료율에 어떤 영향을 주는지 보여 줍니다.

**핵심 개념**: 프롬프트 엔지니어링, 어블레이션 연구, 성능 벤치마킹

### system-hint - 시스템 프롬프트 최적화
`chapter2/system-hint/`

System Hint가 Agent 행동에 미치는 영향을 연구하고, 시스템 프롬프트를 최적화해 성능을 높이는 방법을 살펴봅니다.

**핵심 개념**: 시스템 프롬프트, 행동 유도, 프롬프트 최적화

### log-sanitization - 로그 정제
`chapter2/log-sanitization/`

디버깅 정보는 보존하면서 민감한 데이터를 보호하는 지능형 로그 정제 시스템을 구현합니다.

**핵심 개념**: 개인정보 보호, 로그 처리, 데이터 보안

### prompt-injection - 프롬프트 인젝션 공격과 방어 실험
`chapter2/prompt-injection/`

3가지 공격 시나리오(직접 인젝션, 간접 인젝션, 메모리 인젝션) × 4가지 방어 구성(무방비, 프롬프트 강화, 출처 태깅, 결합 방어)의 통제 실험을 구성합니다. 결정론적 규칙으로 공격 성공률을 계산하여 다층 방어가 인젝션 성공률을 크게 낮추는 모습을 시각적으로 보여 줍니다.

**핵심 개념**: 프롬프트 인젝션, 간접 인젝션, 데이터/지시 분리, 런타임 검증

### agent-skills-ppt - PPT 생성을 위한 Agent Skills 점진적 공개
`chapter2/agent-skills-ppt/`

Agent Skills의 “점진적 공개” 개념을 재현합니다. Agent는 처음에 간략한 Skill 디렉터리만 보고, 작업에 `pptx` Skill이 필요하다고 판단한 뒤에야 전체 워크플로, 상세 문서, 번들 스크립트를 단계적으로 불러옵니다. 마지막에는 python-pptx로 실제 `.pptx` 파일을 생성합니다.

**핵심 개념**: Agent Skills, 점진적 공개, 온디맨드 로딩, 도구 오케스트레이션

## 📚 3장 · 사용자 메모리와 지식 베이스

### user-memory - 사용자 메모리 시스템
`chapter3/user-memory/`

장기 사용자 메모리 시스템을 구축하여 Agent가 사용자 선호와 이전 상호작용을 기억하고 개인화된 서비스를 제공할 수 있게 합니다.

**핵심 개념**: 장기 메모리, 개인화, 사용자 모델링

### mem0 / memobase - 오픈 소스 메모리 프레임워크 비교
`chapter3/mem0/` 및 `chapter3/memobase/`

오픈 소스 메모리 프레임워크인 mem0와 Memobase로 각각 사용자 메모리를 구현합니다. 실험 3-2 “메모리 전략 비교”의 비교 구현으로서, 서로 다른 메모리 솔루션의 추출 형식과 답변 품질을 수평적으로 비교할 수 있습니다.

**핵심 개념**: 메모리 프레임워크, mem0, Memobase, 솔루션 비교

### user-memory-evaluation - 사용자 메모리 평가 프레임워크
`chapter3/user-memory-evaluation/`

여러 테스트 시나리오와 평가 지표를 포함하여 사용자 메모리 시스템의 정확성, 관련성, 효과를 체계적으로 평가합니다.

**핵심 개념**: 평가 프레임워크, 테스트 케이스, 성능 지표

### dense-embedding - 밀집 임베딩 벡터 검색 서비스
`chapter3/dense-embedding/`

벡터 유사도 검색 서비스를 구축하고 ANNOY(트리 기반)와 HNSW(그래프 기반) 근사 최근접 이웃 인덱스 알고리즘을 비교합니다. 성능, 메모리 사용량, 업데이트 가능성 측면에서 서로 다른 인덱싱 전략의 장단점을 보여 줍니다.

**핵심 개념**: 밀집 임베딩, 벡터 검색, ANN 알고리즘, 의미 검색

### sparse-embedding - 희소 검색 엔진
`chapter3/sparse-embedding/`

BM25 알고리즘 기반 희소 벡터 검색 엔진을 처음부터 구현합니다. 용어 빈도 가중치 계산과 역색인 원리를 비롯해 검색 엔진의 내부 동작을 이해할 수 있도록 풍부한 로그와 시각화 인터페이스를 제공합니다.

**핵심 개념**: 희소 임베딩, BM25, TF-IDF, 정확 일치

### retrieval-pipeline - 하이브리드 검색 파이프라인
`chapter3/retrieval-pipeline/`

밀집 검색, 희소 검색, 신경망 재순위화를 결합한 완전한 검색 파이프라인을 구축합니다. 세심하게 설계한 테스트 케이스를 통해 다양한 시나리오에서 하이브리드 검색이 제공하는 상호 보완적 이점을 체계적으로 보여 줍니다.

**핵심 개념**: 하이브리드 검색, 신경망 재순위화, Cross-Encoder, 검색 융합

### multimodal-agent - 멀티모달 정보 추출
`chapter3/multimodal-agent/`

네이티브 멀티모달 처리, 텍스트 변환, 도구 기반 분석이라는 세 가지 멀티모달 처리 전략을 비교합니다. 통합 프레임워크 안에서 어블레이션 연구를 수행해 각 기술 경로의 충실도, 비용, 유연성 간 장단점을 밝힙니다.

**핵심 개념**: 멀티모달, 시각 이해, OCR, 종단 간 처리

### structured-index - 구조화 인덱스
`chapter3/structured-index/`

RAPTOR(재귀적 추상 처리 트리)와 GraphRAG(지식 그래프)라는 두 가지 고급 인덱싱 전략을 구현하고 비교합니다. 인덱싱 기법 안내서를 통해 지식에 내재한 계층 구조와 관계를 반영하는 구조화 인덱스를 구축하는 방법을 보여 줍니다.

**핵심 개념**: RAPTOR, GraphRAG, 계층적 요약, 지식 그래프

### agentic-rag - Agentic RAG
`chapter3/agentic-rag/`

전통적인 Non-Agentic RAG와 Agentic RAG의 성능 차이를 비교합니다. Agent가 ReAct 패턴으로 반복적인 정보 검색을 주도하여 복잡한 사법 질의응답에서 답변 품질을 크게 높이는 모습을 보여 줍니다.

**핵심 개념**: Agentic RAG, ReAct 루프, 반복 검색, 능동 탐색

### agentic-rag-for-user-memory - Agentic RAG로 사용자 메모리 구축
`chapter3/agentic-rag-for-user-memory/`

Agentic RAG 프레임워크로 사용자 대화 기록을 관리합니다. 다중 턴 반복 검색을 활용해 세션을 넘나드는 메모리 검색을 처리하고, 기본적인 회상과 세션 간 검색 역량을 구현합니다.

**핵심 개념**: 사용자 메모리, 대화 기록 인덱싱, 세션 간 검색

### contextual-retrieval - 컨텍스트 검색
`chapter3/contextual-retrieval/`

Anthropic이 제안한 컨텍스트 검색 기법을 구현합니다. 텍스트 청크의 핵심 맥락을 담은 접두 요약을 생성하여 전통적인 청킹 방식의 컨텍스트 손실 문제를 해결하고 검색 실패율을 49~67% 줄입니다.

**핵심 개념**: 컨텍스트 보강, 접두사 생성, 의미 앵커링, 검색 최적화

### contextual-retrieval-for-user-memory - 사용자 메모리 시스템을 위한 컨텍스트 검색
`chapter3/contextual-retrieval-for-user-memory/`

사용자 메모리 구축에 컨텍스트 검색 기법을 적용합니다. Advanced JSON Cards와 Contextual RAG를 결합해 이중 메모리 구조를 만들고 더 높은 수준의 선제적 서비스 역량을 구현합니다.

**핵심 개념**: 이중 메모리, 구조화 사실, 컨텍스트 검색, 선제적 서비스

### structured-knowledge-extraction - 구조화 지식 추출
`chapter3/structured-knowledge-extraction/`

사법 판례를 예로 들어 “상향식 요인 발견 → 사건 프로토타입 클러스터링 → 대화형 자문 Agent”의 3단계 파이프라인을 구현합니다. 미리 정한 경직된 필드 없이 LLM이 수많은 사건에서 요인을 자율적으로 발견하고 모듈형 스키마(핵심 요인 + 혐의별 확장 요인)로 요약합니다. 이후 사건을 여러 프로토타입으로 군집화하고 각 프로토타입에서 요인별 중요도를 계산합니다. Agent는 새로운 사건의 사실관계를 가장 유사한 프로토타입과 연결하고, 요인 중요도에 따라 누락 정보를 질문한 뒤 근거 기반 조언을 제공합니다(법적 고지 포함).

**핵심 개념**: 상향식 지식 발견, 모듈형 요인, 프로토타입 클러스터링, 설명 가능한 의사결정

## 🛠️ 4장 · 도구

### perception-tools - 인식 도구 MCP 서버
`chapter4/perception-tools/`

웹 검색, 멀티모달 이해, 파일 시스템 작업, 공개 데이터 소스 접근 기능을 포괄하는 인식 도구 모음을 구축합니다. 대부분 무료 공개 API(DuckDuckGo, Open-Meteo, Yahoo Finance, OpenStreetMap 등)를 기반으로 하며 API 키가 필요하지 않습니다.

**핵심 개념**: MCP 프로토콜, 멀티모달 파싱, 공개 데이터 소스, 문서 이해, 지리 공간 서비스

### execution-tools - 실행 도구 MCP 서버
`chapter4/execution-tools/`

파일 작업, 코드 인터프리터, 가상 터미널, 외부 시스템 통합 등 안전장치를 갖춘 실행 도구 모음을 구현합니다. 보조 LLM 승인 메커니즘으로 위험한 작업을 방지하고, 복잡한 출력을 자동 요약하며, 코드 구문을 검증합니다.

**핵심 개념**: MCP 프로토콜, 실행 안전성, LLM 승인, 결과 요약, 자동 검증

### collaboration-tools - 협업 도구 MCP 서버
`chapter4/collaboration-tools/`

브라우저 자동화(browser-use 프레임워크), Human-in-the-Loop, 다중 채널 알림(이메일, Telegram, Slack, Discord), 타이머 관리 등 포괄적인 협업 기능을 제공합니다. 민감한 작업에 대한 관리자 승인과 예약 작업 실행을 지원합니다.

**핵심 개념**: MCP 프로토콜, 브라우저 자동화, HITL 모드, 다중 채널 알림, 예약 작업

### agent-with-event-trigger - MCP 통합 이벤트 트리거 Agent
`chapter4/agent-with-event-trigger/`

FastAPI로 구축한 현대적인 이벤트 기반 Agent입니다. 앞의 세 MCP 서버에 있는 모든 도구를 기본으로 통합합니다. 네이티브 비동기 아키텍처로 MCP 도구를 깔끔하게 불러오고, HTTP API를 통해 여러 출처(Web, 인스턴트 메시징, GitHub, 타이머 등)의 이벤트를 수신합니다. 자동 API 문서(Swagger UI)와 백그라운드 모니터링 기능도 제공합니다.

**핵심 개념**: FastAPI, 네이티브 비동기, MCP 통합, 이벤트 기반, 자동 API 문서, 도구 오케스트레이션

### active-tool-selection - 능동적 도구 선택
`chapter4/active-tool-selection/`

미리 정한 도구 집합을 수동적으로 받아들이는 대신, Agent가 작업 요구 사항에 따라 가장 적합한 도구 조합을 능동적으로 선택하는 지능형 메커니즘을 구현합니다.

**핵심 개념**: 도구 선택, 동적 도구 로딩, 작업 분석

### async-agent - 병렬 실행과 중단을 지원하는 비동기 Agent
`chapter4/async-agent/`

단일 스레드 asyncio 모델을 기반으로 이벤트 기반 비동기 Agent 프레임워크(Flux)의 핵심을 구현합니다. 받은 편지함 이벤트 큐가 긴급도(interrupt/immediate/queue)에 따라 작업을 분배하고, 비동기 도구의 병렬 실행, 실행 중 현재 턴 중단, 장기 실행 시뮬레이션 작업의 취소와 상태 조회를 지원합니다. 의사결정에는 실제 LLM(function calling)을 사용합니다.

**핵심 개념**: 비동기 프로그래밍, 이벤트 큐, 중단 메커니즘, 병렬 도구 취소, 논블로킹 I/O

> 이와 함께 `chapter4/docker-compose.yml`과 `chapter4/DOCKER_DEPLOYMENT.md`는 앞서 설명한 MCP 도구 서버를 컨테이너화하고 배포하는 참고 솔루션을 제공합니다.

## 💻 5장 · Coding Agent와 코드 생성

### coding-agent - 프로덕션급 Coding Agent
`chapter5/coding-agent/`

Claude를 기반으로 구축한 프로덕션급 AI 코딩 도우미입니다. 명령줄 의존성 없이 순수 Python으로 완전히 구현했습니다. 파일 작업, 검색, 셸 작업, 프로젝트 관리를 아우르는 17개의 완전한 도구가 포함되며, ripgrep 기능과 완전히 호환되는 순수 Python Grep 도구도 제공합니다.

**주요 기능**:

- 명령줄 의존성이 없는 순수 Python 구현으로, 특히 Mac 사용자에게 적합
- 파일 읽기/쓰기/편집, 순수 Python 정규식 검색, 디렉터리 목록, 셸 세션 관리 등 완전한 도구 모음
- 타임스탬프, 도구 호출 횟수 계산, TODO 목록 관리, 상세 오류 메시지 등의 시스템 프롬프트 기법
- 영구 셸 환경, 자동 린트 감지, 스트리밍 응답 지원
- 여러 LLM 공급자(Anthropic, OpenAI, OpenRouter) 지원

**핵심 개념**: 코드 생성, 파일 편집, 순수 Python 도구, 시스템 프롬프트, 린트 감지, 다중 공급자 지원

### code-for-math - 코드로 수학 문제 해결 능력 향상
`chapter5/code-for-math/`

같은 모델과 같은 경시 수학 문제 집합으로 “순수 사고 연쇄”와 “코드 보조” 모드를 비교합니다. 코드 보조 모드에서는 문제를 Python(sympy/numpy/scipy)으로 형식화하고 하위 프로세스 샌드박스에서 function calling으로 실행합니다. 오류가 잦은 암산을 정확한 계산으로 대체해 정확도를 크게 높입니다.

**핵심 개념**: 코드 인터프리터, 기호 계산, 사고 연쇄 비교, 도구 증강 추론

### code-for-logic - 코드로 논리적 추론 능력 향상
`chapter5/code-for-logic/`

“기사와 악당” 논리 퍼즐을 제약 충족 문제(CSP)로 변환합니다. Agent가 `python-constraint`로 변수와 쌍조건 제약을 정의한 뒤 솔버를 호출합니다. K&K 퍼즐 집합에서 순수 자연어 추론과 코드 보조 모드의 정확도를 비교합니다.

**핵심 개념**: 제약 조건 풀이, CSP 모델링, 형식화 추론, 코드 보조

### small-model-codified-rules - 소형 모델을 위한 코드화 규칙
`chapter5/small-model-codified-rules/`

τ-bench 항공사 고객 서비스 시나리오를 기반으로 한 통제 실험입니다. 복잡한 업무 정책(환불 규칙)을 자연어 프롬프트에서 코드/도구로 옮기자 소형 모델의 작업 성공률과 정책 준수율이 크게 향상되었습니다. 도구 내부의 코드 검증은 모델의 잘못된 판단을 실시간으로 차단할 수 있습니다.

**핵심 개념**: 코드화된 업무 규칙, 정책 집행, 도구 내부 검증, 소형 모델 신뢰성

### paper-to-ppt - 논문에서 PPT 자동 생성(Proposer-Reviewer)
`chapter5/paper-to-ppt/`

“PPT 만들기”를 코드 생성 문제로 재구성합니다. Proposer가 Slidev(Markdown+HTML) 코드를 작성하면 Reviewer가 각 페이지를 PNG로 렌더링하고 Vision LLM으로 레이아웃 문제를 검사한 뒤, 구조화 피드백을 바탕으로 반복 수정합니다. 이중 Agent 분업으로 최대 컨텍스트 크기를 크게 줄입니다.

**핵심 개념**: 코드 생성, Slidev, Proposer-Reviewer, 시각 품질 관리

### paper-to-video - 논문 설명 영상 자동 생성
`chapter5/paper-to-video/`

“논문 → PPT”를 바탕으로 슬라이드마다 구어체 내레이션 대본을 생성하고 TTS로 음성을 합성합니다. 이어 ffmpeg로 각 슬라이드의 스크린샷과 오디오를 페이지별로 동기화하여 내레이션이 포함된 설명 영상을 만듭니다.

**핵심 개념**: 멀티미디어 생성, 내레이션 대본 생성, TTS, ffmpeg 오디오·비디오 동기화

### video-edit - API 기반 지능형 영상 편집
`chapter5/video-edit/`

여러 장면이 있는 영상과 자연어 요청이 주어지면 Agent가 “2단계 Vision 위치 탐색”(거친 단계에서 세밀한 단계로 프레임 추출 및 판독)을 사용해 대상 장면의 시간 경계를 찾습니다. 구간을 자른 뒤 Reviewer가 결과 클립에서 키프레임을 추출해 검증하고, 결과가 만족스럽지 않으면 다시 수정합니다.

**핵심 개념**: 영상 편집, Vision 위치 탐색, 거친 단계에서 세밀한 단계로, Proposer-Reviewer

### adaptive-log-parser - 적응형 로그 파싱 시스템
`chapter5/adaptive-log-parser/`

스스로 진화하는 로그 파싱 시스템입니다. 파싱할 수 없는 새로운 형식을 만나도 오류를 내지 않고, 실패한 샘플과 오류 메시지를 코드 생성 Agent에 전달해 `parse` 함수를 만듭니다. 자동 테스트를 통과하면 함수를 핫 업데이트하여 파싱 엔진에 등록하므로 전체 과정에 사람의 개입이 필요하지 않습니다.

**핵심 개념**: 시스템 어댑터로서의 코드, 자기 복구 루프, 코드 핫 업데이트, 자동 테스트

### log-diagnosis - 프로덕션 로그 지능형 진단 시스템
`chapter5/log-diagnosis/`

진단 Agent가 프로덕션 추적 로그, 아키텍처 문서, PRD를 읽습니다. 문제와 근본 원인을 자동으로 찾고 구조화 보고서와 회귀 테스트 케이스를 생성하며, 재생 프레임워크로 실제 실행을 검증합니다. MCP 통합을 통해 GitHub Issue 생성도 모의 실행합니다.

**핵심 개념**: 추적 진단, 근본 원인 위치 탐색, 회귀 테스트 생성, 재생 검증

### dynamic-form - 의도 명확화를 위한 동적 양식
`chapter5/dynamic-form/`

불완전한 요청을 받았을 때 Agent가 질문을 하나씩 하지 않고 연쇄 로직이 포함된 독립형 HTML 양식을 동적으로 생성하여, 사용자가 누락된 정보를 한 번에 입력하게 합니다. 프런트엔드는 양식 데이터를 JSON으로 모아 Agent에 반환하고 작업을 계속합니다.

**핵심 개념**: 코드 생성, 의도 명확화, 동적 양식, 연쇄 로직

### erp-agent - 자연어 ERP Agent(NL → SQL)
`chapter5/erp-agent/`

중국어 자연어 질의를 SQL로 변환해 데이터베이스에서 실행하고 결과 표를 바로 표시합니다. 핵심은 LLM이 데이터 자체를 옮기지 않고 SQL 아티팩트만 생성하는 아티팩트 패턴입니다. 토큰을 절약하고 수동 계산 오류를 피하며, 수만 행의 결과 집합도 즉시 반환할 수 있습니다.

**핵심 개념**: NL2SQL, 아티팩트 패턴, 데이터베이스 실행, 비용과 정확성

### conversational-ui - 대화형 UI 사용자화 시스템
`chapter5/conversational-ui/`

사용자가 색상·글꼴·텍스트·레이아웃 변경을 자연어로 요청하면 Agent가 React 프런트엔드 소스 코드를 자율적으로 찾아 수정합니다. Vite의 Hot Module Replacement(HMR)를 활용해 변경 사항이 즉시 반영되며, 다중 턴 반복 사용자화를 지원합니다.

**핵심 개념**: 코드 수정, 프런트엔드 사용자화, 핫 리로딩, 다중 턴 반복

## 🎯 6장 · Agent 평가

### terminal-bench - 터미널 환경 벤치마크
`chapter6/terminal-bench/`

Terminal-Bench는 실제 터미널 환경에서 AI Agent의 성능을 시험하는 벤치마크입니다. 코드 컴파일부터 모델 학습과 서버 설정까지, Agent가 실제 종단 간 작업을 처리하는 능력을 평가합니다. 약 100개 작업의 데이터셋과 실행 프레임워크가 포함되어 여러 Agent 구현을 지원합니다.

**핵심 개념**: 터미널 자동화, 작업 평가, Docker 샌드박스, 벤치마킹

### SWE-bench - 소프트웨어 엔지니어링 벤치마크
`chapter6/SWE-bench/`

SWE-bench는 대규모 언어 모델이 실제 GitHub Issue를 해결하는 능력을 평가하는 벤치마크입니다. 코드베이스와 Issue 설명이 주어지면 모델은 문제를 해결하는 패치를 생성해야 합니다. SWE-bench, SWE-bench Lite, SWE-bench Verified, SWE-bench Multimodal 등 여러 버전이 있습니다.

**핵심 개념**: 코드 수정, GitHub Issue, 패치 생성, Docker 평가

### GAIA - 범용 AI 도우미 벤치마크
`chapter6/GAIA/`

GAIA는 차세대 LLM(도구 증강, 효율적 프롬프팅, 검색 접근 등을 갖춘 모델)을 평가합니다. 여러 수준의 도구 사용과 자율성이 필요하고 정답이 명확한 450개 이상의 비단순 질문이 있으며, 세 단계 난도로 나뉩니다.

**핵심 개념**: 도구 사용, 다단계 추론, 자율성 평가

### OSWorld - 운영체제 수준 Agent 벤치마크
`chapter6/OSWorld/`

파일 관리, 애플리케이션 조작, 시스템 설정을 포함해 완전한 운영체제 환경 안에서 복잡한 작업을 수행하는 Agent의 능력을 평가합니다.

**핵심 개념**: 운영체제 자동화, 다중 애플리케이션 협업, 시스템 수준 작업

### android_world - Android 환경 벤치마크
`chapter6/android_world/` (📖 외부 저장소, “외부 저장소 가져오기” 참고)

앱 탐색, UI 상호작용, 작업 완료 역량을 포함해 Android 모바일 환경에서 Agent의 성능을 평가합니다.

**핵심 개념**: 모바일 자동화, Android UI, 애플리케이션 상호작용

> 하이픈을 사용한 `chapter6/android-world/`는 벤치마크 코드가 아니라 android_world에서 T3A Agent가 실패한 사례에 관한 책의 분석 노트(`t3a*.md`)이며, 참고 자료로 읽을 수 있습니다.

### tau2-bench - 도구 증강 추론 벤치마크
`chapter6/tau2-bench/`

계산, 검색, 데이터 처리 등의 시나리오를 포함해 Agent가 도구를 사용하여 복잡한 추론을 수행하는 능력을 중점적으로 평가합니다.

**핵심 개념**: 도구 증강 추론, 다단계 작업, 도구 조합

### elo-leaderboard - ELO 리더보드 시스템
`chapter6/elo-leaderboard/`

ELO 평점 체계에 기반한 Agent 성능 리더보드를 구현하고, 쌍대 비교를 통해 서로 다른 Agent의 상대적 역량을 평가합니다.

**핵심 개념**: ELO 평점, 상대 평가, 리더보드 시스템

### model-benchmark - 다차원 모델 성능 벤치마크
`chapter6/model-benchmark/`

여러 OpenAI 호환 LLM API 공급자를 수평 비교합니다. 스트리밍 인터페이스로 첫 토큰까지 걸리는 시간(TTFT)을 정밀 측정하고, 동시 요청 상황의 종단 간 지연 시간 백분위수(p50/p95), 처리량, 성공률을 계산합니다. 단일 명령으로 다차원 비교표를 만들어 모델 선택이 리더보드만 보는 문제가 아니라 여러 요소의 절충임을 보여 줍니다.

**핵심 개념**: TTFT, 지연 시간 백분위수, 처리량, 동시성 스트레스 테스트, 모델 선택

### agent-cost-analysis - 종단 간 Agent 작업 비용 분석
`chapter6/agent-cost-analysis/`

일반적인 다중 턴 Agent 작업(고객 서비스 환불)의 전체 비용을 단계별로 분석합니다. 자체 경량 추적 시스템으로 각 LLM 호출의 입력/출력/캐시 토큰, 지연 시간, 비용을 기록하고 집계해 “어느 단계가 가장 비싼지” 찾은 뒤, A/B 테스트로 KV Cache 친화적 설계와 컨텍스트 압축의 실제 절감 효과를 정량화합니다.

**핵심 개념**: 관측 가능성, 비용 분석, 프롬프트 캐싱, A/B 비교

### tts-quality-eval - 완전 자동화 TTS 품질 평가 파이프라인
`chapter6/tts-quality-eval/`

여러 TTS 구성(서로 다른 모델/음성/속도)으로 동일한 난도 높은 텍스트 집합을 합성한 뒤, 멀티모달 LLM-as-a-Judge가 Rubric에 따라 각 항목(명료성, 자연스러움 등)을 평가합니다. 결과를 집계해 재현 가능한 구성 비교표를 만듭니다.

**핵심 개념**: LLM-as-a-Judge, Rubric 채점, TTS 평가, 다차원 비교

## 🧠 7장 · 모델 사후 학습

이 장에는 지도 미세 조정(SFT)과 강화 학습(RL)의 여러 기법과 적용 시나리오를 다루는 모델 사후 학습 프로젝트가 포함되어 있습니다.

### AdaptThink - 적응형 추론 깊이
`chapter7/AdaptThink/` 및 `chapter7/AdaptThink-original/`

추론 모델이 문제 난도에 따라 추론 모드(Thinking 또는 NoThinking)를 적응적으로 선택하도록 학습합니다. 제약 최적화와 중요도 샘플링으로 정확도를 높이면서 추론 비용을 45~69% 크게 줄입니다. DeepSeek-R1-Distill-Qwen 모델을 기반으로 DAPO 알고리즘을 사용해 학습합니다.

**핵심 개념**: 적응형 추론, 추론 비용 최적화, 제약 최적화, 중요도 샘플링

### retool - 도구 증강 수학 추론
`chapter7/retool/`

다중 턴 대화와 코드 샌드박스로 대규모 언어 모델의 수학 추론 능력을 높입니다. SFT와 RL의 2단계 학습을 통해 모델이 코드 실행 환경을 활용해 수학 문제를 풀도록 합니다. Qwen2.5-32B-Instruct를 기반으로 AIME 2024 데이터셋, DAPO 알고리즘, SandboxFusion 샌드박스를 사용합니다.

**핵심 개념**: 도구 사용, 코드 실행, 수학 추론, 다중 턴 대화, DAPO 알고리즘

### AWorld / AWorld-train - 체화 Agent 학습
`chapter7/AWorld/` 및 `chapter7/AWorld-train/`

AWorld 프레임워크를 기반으로 체화 Agent를 학습하여 가상 환경에서 복잡한 작업을 수행하고 경험으로부터 배우게 합니다.

**핵심 개념**: 체화 지능, 환경 상호작용, 경험 학습

### SFTvsRL - SFT와 RL 비교 연구
`chapter7/SFTvsRL/`

여러 작업에서 지도 미세 조정(SFT)과 강화 학습(RL)의 효과를 체계적으로 비교하고 두 방법의 장단점과 적합한 적용 시나리오를 분석합니다.

**핵심 개념**: SFT와 RL, 학습 방법 비교, 성능 분석

### verl - 효율적인 RL 학습 프레임워크
`chapter7/verl/`

verl은 대규모 언어 모델의 RLHF 학습을 위해 특별히 설계한 효율적인 강화 학습 프레임워크로, PPO, GRPO, DAPO 등 여러 알고리즘을 지원합니다.

**핵심 개념**: RLHF, PPO, 분산 학습, 효율적 최적화

### Intuitor - 직관적 추론 학습
`chapter7/Intuitor/`

모델의 직관적 추론 능력을 학습하여 상세한 사고 연쇄 없이도 빠르고 합리적인 판단을 내리게 합니다.

**핵심 개념**: 직관적 추론, 빠른 의사결정, 사고 연쇄 최적화

### MultilingualReasoning - 다국어 추론
`chapter7/MultilingualReasoning/`

다국어 환경에서 모델의 추론 능력을 학습하여 언어 간 작업의 성능을 높입니다.

**핵심 개념**: 다국어, 언어 간 추론, 언어 일반화

### SpatialReasoning - 공간 추론 학습
`chapter7/SpatialReasoning/`

위치, 방향, 거리 같은 공간 관계 문제를 처리하도록 모델의 공간 추론 능력을 중점적으로 학습합니다.

**핵심 개념**: 공간 추론, 기하학적 이해, 위치 관계

### SimpleVLA-RL - 시각·언어·행동 RL
`chapter7/SimpleVLA-RL/`

강화 학습에서 시각, 언어, 행동을 결합하여 모델이 시각 입력을 이해하고 그에 맞는 행동을 수행하게 합니다.

**핵심 개념**: 시각·언어·행동, 멀티모달 RL, 체화 지능

### continued-pretraining - 지속 사전 학습
`chapter7/continued-pretraining/`

도메인별 데이터로 지속 사전 학습을 수행해 대상 도메인에서 모델 성능을 높입니다.

**핵심 개념**: 지속 사전 학습, 도메인 적응, 지식 주입

### MiniMind-pretrain - 소형 모델 사전 학습
`chapter7/MiniMind-pretrain/`

소형 언어 모델을 처음부터 사전 학습하여 전체 사전 학습 과정과 핵심 기술을 이해합니다.

**핵심 개념**: 사전 학습, 소형 모델, 학습 파이프라인

### sesame - 시퀀스 모델링과 평가
`chapter7/sesame/`

시퀀스 모델링 작업의 학습 및 평가 방법에 집중합니다.

**핵심 개념**: 시퀀스 모델링, 평가 방법, 성능 최적화

### orpheus - 음악 생성과 이해
`chapter7/orpheus/`

음악 생성과 이해를 위한 모델을 학습합니다.

**핵심 개념**: 음악 생성, 오디오 이해, 창의적 AI

### tinker-cookbook - 학습 팁 모음
`chapter7/tinker-cookbook/`

모델 학습에 관한 여러 실용적인 팁과 모범 사례를 모았습니다.

**핵심 개념**: 학습 팁, 모범 사례, 튜닝 방법

## 🔄 8장 · Agent 자기 진화

이 장은 가중치를 수정하지 않고 Agent가 경험으로부터 계속 성장하도록 하는 데 집중합니다. 성공한 궤적을 재사용 가능한 경험으로 정제하고, 반복 작업을 도구로 외부화하며, 프롬프트와 관찰을 모델에 증류합니다.

### gaia-experience - 성공 경험으로부터 학습
`chapter8/gaia-experience/`

AWorld 프레임워크와 GAIA 벤치마크를 기반으로 완전한 “학습-적용” 루프를 구현합니다. Agent가 성공한 작업 궤적을 구조화된 경험으로 자동 요약하고 새로운 작업에서 검색·적용하여 자기 진화를 달성합니다.

**핵심 개념**: 경험 학습, 전략 요약, 궤적 요약, 자기 진화

### browser-use-rpa - 워크플로 기록과 재생
`chapter8/browser-use-rpa/`

브라우저 자동화의 워크플로 기록 시스템을 구현하여 반복적인 작업 시퀀스를 매개변수화된 도구로 자동 캡슐화합니다. 비용이 많이 드는 LLM 추론을 정밀한 자동 실행으로 전환해 속도를 3~5배 높입니다.

**핵심 개념**: 워크플로 기록, RPA, 도구 생성, 외부화 학습

### prompt-distillation - 프롬프트 증류
`chapter8/prompt-distillation/`

복잡한 프롬프트의 효과를 모델 매개변수로 증류하여 추론 시 프롬프트 길이를 줄이고, 컨텍스트 경험을 매개변수화된 지식으로 고정합니다.

**핵심 개념**: 지식 증류, 프롬프트 최적화, 매개변수화된 지식

### prompt-auto-optimization - 시스템 프롬프트 자동 최적화
`chapter8/prompt-auto-optimization/`

사람의 피드백에 기반한 자동 시스템 프롬프트 학습입니다. tau-bench 스타일 항공사 고객 서비스의 “과도한 이관” 문제를 예로 들어, Coding Agent가 시스템 프롬프트 파일을 읽고 문제가 있는 규칙을 찾아 정확한 수정안을 생성한 뒤 실제로 프롬프트 파일을 다시 씁니다. 이어 변경 사항을 재평가하여 “피드백 → 재작성 → 검증” 루프를 만듭니다.

**핵심 개념**: 프롬프트 자동 최적화, 사람의 피드백, Coding Agent, 폐쇄 루프 평가

### active-tool-discovery - 능동적 도구 발견
`chapter8/active-tool-discovery/`

“120개 이상의 도구 스키마를 모두 주입”하는 방식과 “필요할 때 능동적으로 발견”하는 방식을 비교합니다. 후자는 시스템 프롬프트에 몇 개의 기본 도구와 `discover_tools` 메타 도구만 유지하고, 임베딩 유사도로 도구 라이브러리에서 가장 관련성이 높은 전문 도구 3~5개를 검색합니다. 이를 통해 토큰을 절약하고 지나치게 긴 목록 때문에 모델이 범용 도구를 잘못 선택하거나 오용하는 일을 방지합니다.

**핵심 개념**: 능동적 도구 발견, 임베딩 검색, 토큰 최적화, 지시 이행

### self-evolving-tools - 웹에서 도구를 찾아 자기 진화
`chapter8/self-evolving-tools/`

Alita 스타일의 “최소한의 사전 정의, 최대한의 자기 진화” 접근법입니다. Agent에는 미리 만든 도메인별 도구 없이 다섯 개의 범용 메타 도구만 있습니다. 수행할 수 없는 작업을 만나면 웹에서 오픈 소스 라이브러리/API를 검색하고, 문서를 읽고, 샌드박스에서 시험합니다. 가능한 솔루션을 새 도구로 캡슐화해 도구 라이브러리에 저장하고 재사용하며, 전체 과정에서 환각 제어를 강조합니다.

**핵심 개념**: 자기 진화, 도구 제작, 도구 재사용, 환각 제어

### self-evolution-eval - 자기 진화 Agent 평가 데이터셋
`chapter8/self-evolution-eval/`

Agent가 스스로 도구를 발견·제작·재사용하는 “자기 진화” 역량을 평가하도록 설계한 전용 데이터셋과 검증 방법론입니다. 도구 이름을 알려 주지 않는 20개의 도메인 간 작업, 4계층 검증 하네스, 제어 가능한 참조 Agent로 구성됩니다. “결과가 맞는가”만 확인하지 않고 발견·제작·재사용의 품질을 평가합니다.

**핵심 개념**: 평가 데이터셋 설계, 계층적 검증, 도구 재사용 지표, 자기 진화

## 🎙️ 9장 · 멀티모달과 실시간 상호작용

### live-audio - 실시간 음성 대화
`chapter9/live-audio/`

음성 인식, AI 대화, 음성 합성을 통합한 실시간 음성 채팅 데모입니다. 여러 AI 서비스 공급자(OpenAI, OpenRouter, ARK, Siliconflow)를 지원하여 지연 시간이 짧은 대화 경험을 제공합니다.

**주요 기능**:

- VAD(Voice Activity Detection)를 이용한 실시간 음성 입력
- 다중 공급자 지원: ASR(OpenAI Whisper, SenseVoice), LLM(GPT-4o, Gemini, Doubao), TTS(Fish Audio)
- WebSocket 실시간 통신과 저지연 오디오 스트리밍
- 실시간 지연 시간 모니터링과 로깅

**핵심 개념**: 음성 인식, 실시간 대화, TTS, WebSocket, 다중 공급자 아키텍처

### browser-use - 브라우저 자동화 Agent(Computer Use)
`chapter9/browser-use/`

Browser-Use는 LLM이 브라우저를 제어하여 복잡한 작업을 완료하게 하는 강력한 브라우저 자동화 프레임워크입니다. 양식 입력, 웹 탐색, 데이터 추출 등의 시나리오를 지원하며 GUI 자동화(Computer Use)의 대표적 구현입니다.

**주요 기능**:

- LLM 기반 브라우저 자동화
- 여러 LLM 지원(ChatBrowserUse, OpenAI, Google, 로컬 모델)
- 사용자 정의 도구 확장과 인증 처리
- 샌드박스 배포와 클라우드 서비스 통합 지원

**핵심 개념**: 브라우저 자동화, Computer Use, 시각 이해, 도구 확장

### claude-quickstarts - Claude 빠른 시작
`chapter9/claude-quickstarts/`

다양한 사용 사례를 다루는 Claude API 빠른 시작 예제와 모범 사례입니다.

**핵심 개념**: Claude API, 프롬프트 엔지니어링, 모범 사례

### phone-agent - 전화 Agent
`chapter9/phone-agent/`

“사용자를 대신해 전화로 외부 세계와 상호작용하는” 음성 Agent를 보여 줍니다. 상위 계층은 표준 ReAct Agent입니다. 자연어 작업을 받으면 통화 횟수와 목적을 자율적으로 정하고, 전화 API 추상화에 기반한 `make_phone_call` 도구를 호출해 전체 대화를 완료합니다. 구조화된 통화 기록을 읽고 필요하면 다시 전화해 추가 질문을 한 뒤 최종 결과를 사용자에게 보고합니다.

**핵심 개념**: 음성 Agent, 전화 상호작용, ReAct, 도구 추상화

### end-to-end-speech - 종단 간 음성 사고와 캐스케이드 파이프라인 비교
`chapter9/end-to-end-speech/`

Step-Audio R1의 종단 간 음성 추론 패러다임(단일 모델의 “듣기 → 생각하기 → 말하기”)에 대응합니다. “음성 입력 → 사고 → 음성 출력” 폐쇄 루프를 실행하고, 캐스케이드형 ASR→LLM→TTS 패러다임과 지연 시간 및 준언어 정보(감정/어조/말하기 속도) 손실을 직관적으로 비교합니다.

**핵심 개념**: 종단 간 음성, 캐스케이드 비교, 준언어 정보, 말하면서 생각하기

### streaming-speech - 스트리밍 음성 인식 시뮬레이션
`chapter9/streaming-speech/`

스트리밍 음성 인식의 핵심 절충을 보여 줍니다. 연속 오디오를 점점 길어지는 조각으로 나누어 ASR에 입력하고, 조각을 받을 때마다 “현재 부분 인식 결과”를 생성해 매우 짧은 첫 조각 지연 시간으로 텍스트를 일찍 출력합니다. 다만 초반 조각에는 문장 후반부의 맥락이 없어 오류가 발생할 수 있고, 오디오가 누적되면서 점차 올바른 결과로 수렴합니다. 이는 “문장 전체를 기다린 뒤 인식”하는 고정확도·고지연 방식과 대비됩니다.

**핵심 개념**: 스트리밍 인식, 조각 단위 인식, 첫 조각 지연 시간, 성급한 판단의 비용

### controllable-tts - 제어 토큰 기반 제어 가능 TTS
`chapter9/controllable-tts/`

메인 LLM의 출력에 제어 토큰(감정/말하기 속도/스타일/멈춤/웃음)을 포함합니다. 실행 계층은 토큰을 파싱하고 참조 음성 라이브러리의 해당 스타일 프로필에 연결한 뒤 음성을 합성합니다. “어디서 멈추고 어떤 어조를 사용할지”에 관한 판단을 LLM에 맡겨 같은 텍스트를 서로 다른 스타일과 감정으로 합성할 수 있습니다.

**핵심 개념**: 제어 가능 TTS, 제어 토큰, 참조 음성 라이브러리, 운율 제어

## 🤝 10장 · 다중 Agent 협업

### use-computer-while-calling - 이중 Agent 아키텍처
`chapter10/use-computer-while-calling/` (📖 전체 코드는 [19PINE-AI/TalkAct](https://github.com/19PINE-AI/TalkAct)로 분리되었으며, 이 디렉터리에는 문서만 남아 있습니다.)

전화 통화 Agent와 Computer Use Agent로 구성된 이중 Agent 협업 아키텍처를 구현합니다. 두 Agent는 조정자 없이 WebSocket으로 직접 통신합니다. Phone Agent는 음성 상호작용을, Computer Agent는 브라우저 자동화를 담당하며, 음성과 웹 작업이 모두 필요한 복잡한 작업을 병렬로 완료합니다.

**주요 기능**:

- Agent 간 직접 통신(조정자 없음)
- 메시지 전달에 표준 도구 호출 사용
- 병렬 작업: 음성 대화 + 브라우저 자동화
- 간단한 JSON 메시지 프로토콜

**아키텍처 구성 요소**:

- Phone Call Agent(Node.js): 음성 입출력, ASR/TTS, LLM 대화
- Computer Use Agent(Python): 브라우저 자동화, browser-use, 웹 스크래핑
- WebSocket 통신: Agent 간 직접 메시지 전달

**핵심 개념**: 다중 Agent 협업, Agent 간 통신, 병렬 작업 처리, 음성 + 브라우저 통합

### staged-system-prompt - 실행 단계별 시스템 프롬프트 전환
`chapter10/staged-system-prompt/`

같은 Coding Agent가 작업의 실행 단계(요구 사항 명확화 → 코드 구현 → 코드 리뷰)에 따라 서로 다른 시스템 프롬프트와 도구 집합을 불러옵니다. 한 대화 안에서 서로 다른 역할과 행동을 수행하면서도 단계 간 대화 기록과 작업 상태를 계속 공유할 수 있습니다. 리뷰에 실패하면 구현 단계로 돌아갈 수도 있습니다.

**핵심 개념**: 단계별 프롬프트, 역할 전환, 공유 컨텍스트, 단계 파이프라인

### multi-role-transfer - 다중 역할 전환과 자율적 인계
`chapter10/multi-role-transfer/`

공유 컨텍스트에서 연쇄적으로 인계하는 방식을 보여 줍니다. 하나의 세션에 각자 고유한 시스템 프롬프트와 전용 도구 집합을 가진 여러 전문 역할 Agent가 있습니다. Agent는 `transfer_to_agent` 도구를 사용해 작업 진행 상황에 따라 다른 역할로 전환할 시점을 자율적으로 결정합니다. 동일한 대화 기록을 공유하므로 인계 과정에서도 전체 컨텍스트가 자연스럽게 유지됩니다.

**핵심 개념**: 역할 인계, 핸드오프, 공유 컨텍스트, 자율 전환

### book-translation - 책 번역 Agent(오케스트레이터 모드)
`chapter10/book-translation/`

오케스트레이터 모드로 긴 문서 번역을 용어집·번역·교정 전문 Agent의 작업으로 분해합니다. Manager는 작업, 계획, 호출 기록, 파일 인덱스만 저장하고 완성된 번역문은 디스크에 기록하여 컨텍스트 크기를 거의 일정하게 유지합니다. 이를 단일 Agent 방식과 비교하고 실제 토큰 수를 이용해 컨텍스트 폭증을 제어하는 방법과 공유 용어집으로 책 전체의 일관성을 보장하는 방법을 보여 줍니다.

**핵심 개념**: 오케스트레이터 모드, 컨텍스트 격리, 컨텍스트 폭증 제어, 공유 용어집

### parallel-web-research - 병렬 다중 출처 정보 수집 Agent
`chapter10/parallel-web-research/`

중앙 조정 아래 여러 동종 Agent가 병렬 검색하는 방식을 보여 줍니다. 주 조정자가 N개의 하위 Agent를 동시에 실행하고 각 Agent는 한 출처에서 답을 찾습니다. 하나가 목표를 찾으면 나머지는 정상적으로 종료합니다. 메시지 버스, 병렬 분배, 실시간 모니터링, 연쇄 종료, 경쟁 상태 처리를 모두 사실적으로 구현했습니다(실제 브라우저 대신 제어 가능한 모의 정보 출처 사용).

**핵심 개념**: 병렬 Agent, 중앙 조정, 메시지 버스, 연쇄 종료

### voice-werewolf - 음성 마피아 게임 Agent 시스템
`chapter10/voice-werewolf/`

다중 Agent 마피아 게임으로 “비공유 컨텍스트”의 정보 접근 제어를 보여 줍니다. 각 플레이어는 비공개 컨텍스트가 엄격히 격리된 독립 LLM Agent입니다. 코드 기반 결정론적 심판이 어느 정보를 어느 플레이어의 컨텍스트에 전달할지 결정하고 감사용으로 등록하며, 게임 종료 시 격리가 올바른지 자동 검증합니다. 음성은 선택적 확장 기능입니다.

**핵심 개념**: 정보 비대칭, 비공개 컨텍스트 격리, 심판 오케스트레이션, 감사 검증

## 📖 학습 제안

### 핵심 개념: Agent = 모델 + 컨텍스트 + 도구

이 책의 핵심 프레임워크는 **Agent = 모델 + 컨텍스트 + 도구**입니다. 세 구성 요소가 협력하여 Agent의 지능적 행동을 구현합니다.

- **모델**: 이해, 추론, 의사결정 역량을 제공하는 Agent의 두뇌입니다.
- **컨텍스트**: 시스템 지시, 대화 기록, 추론 과정, 도구 상호작용 기록 등을 담는 Agent의 운영체제입니다.
- **도구**: 환경을 인식하고 행동을 실행하며 외부 세계와 상호작용하게 하는 Agent의 손입니다.

### 학습 경로

학습 경로는 책 전체의 장과 일대일로 대응하며 세 가지 축을 중심으로 차근차근 전개됩니다.

- **1장 · 기초**: Agent 시스템의 완전한 인식 체계를 세웁니다. RL에서 Agent의 정의를 이해하고, 전통적 RL과 LLM+RL 패러다임의 샘플 효율 차이를 비교하며, “모델이 곧 Agent”라는 새로운 패러다임과 **Agent = 모델 + 컨텍스트 + 도구**라는 핵심 프레임워크를 익힙니다. **핵심 통찰**: 사전 지식의 중요성은 알고리즘과 환경을 능가합니다.

- **2~3장 · 컨텍스트**: 컨텍스트는 Agent의 운영체제입니다. 2장은 시스템 프롬프트, KV Cache 친화적 설계, 컨텍스트 압축, 프롬프트 엔지니어링 어블레이션 실험을 다룹니다. 3장은 사용자 메모리, 밀집/희소/하이브리드 검색, Agentic RAG, 컨텍스트 검색, 구조화 지식 추출을 다룹니다. **핵심 통찰**: 완전한 컨텍스트에는 시스템 지시, 대화 기록, 추론 과정, 도구 상호작용 기록, 사용자 메모리, 외부 지식이 포함됩니다.

- **4~5장 · 도구**: 도구는 Agent가 세계와 상호작용하는 다리입니다. 4장은 세 가지 MCP 도구(인식/실행/협업), 이벤트 트리거, 비동기 아키텍처를 다룹니다. 5장은 프로덕션급 Coding Agent의 완전한 구현을 깊이 살펴봅니다. **핵심 통찰**: 도구는 범용적으로 설계해야 하며(계산기보다 코드 인터프리터가 낫습니다), 코드는 새 도구를 만드는 메타 역량입니다.

- **6~7장 · 모델**: 지능을 측정하고 증폭하는 방법입니다. 6장은 Terminal-Bench, SWE-bench, GAIA, OSWorld, Tau2-Bench 같은 평가 벤치마크를 다룹니다. 7장은 SFT, RL, RLHF, 샘플 효율 등의 사후 학습 기법을 다룹니다. **핵심 통찰**: 독립적인 검증 신호는 “모델에게 다시 생각해 보라고 요청”하는 것보다 신뢰할 수 있습니다. “모델이 곧 Agent”라는 패러다임은 RL을 통해 도구 호출을 네이티브 역량으로 내재화합니다.

- **8장 · 자기 진화**: 경험 학습, 워크플로의 도구 외부화, 프롬프트와 관찰의 매개변수 증류를 통해 가중치를 바꾸지 않고 Agent가 경험으로부터 성장하게 합니다. **핵심 통찰**: 경험으로부터의 학습은 Agent가 “똑똑한” 상태에서 “숙련된” 상태로 나아가는 열쇠입니다.

- **9~10장 · 확장과 협업**: 9장은 인식과 행동을 텍스트에서 음성, GUI, 물리 세계로 확장합니다. 10장은 다중 Agent의 분업으로 복잡한 작업을 처리합니다. **핵심 통찰**: 다중 Agent 시스템의 모든 설계 결정은 단일 Agent의 세 요소에서 대응 관계를 찾을 수 있습니다.

### 난도

- **초급**(1~2장): 기본 개념을 이해하려는 입문자에게 적합합니다.
- **중급**(3~4장): 어느 정도의 프로그래밍 기초가 필요하며 시스템 통합을 다룹니다.
- **고급**(5~6장): 탄탄한 프로그래밍 역량이 필요하며 복잡한 시스템 설계를 다룹니다.
- **전문가**(7~8장): 딥러닝과 학습/자기 진화 경험이 필요합니다.
- **응용**(9~10장): 앞에서 배운 내용을 종합하여 실제 애플리케이션을 구축합니다.

### 실습 제안

1. **직접 실습하기**: 각 프로젝트는 독립 실행을 염두에 두고 설계했습니다. 직접 코드를 실행하고 수정해 보세요.
2. **책과 함께 보기**: 이 저장소의 [`book-en/`](book-en/) 디렉터리(영어) 또는 [`book/`](book/) 디렉터리(중국어 원문)에서 해당 장을 읽으며 이론과 실습의 결합을 이해하세요.
3. **실험 비교하기**: 여러 프로젝트에 어블레이션 연구와 비교 실험이 포함되어 있습니다. 비교를 통해 이해를 깊게 하세요.
4. **단계적으로 학습하기**: 간단한 프로젝트에서 시작해 점차 복잡한 시스템으로 들어가세요.
5. **프로토콜에 주목하기**: 4장의 MCP 서버 프로젝트는 확장 가능한 Agent를 구축하는 핵심인 표준화 도구 프로토콜을 보여 줍니다.

## 🔑 API 키

편리한 학습을 위해 여러 플랫폼에서 API 키를 발급받는 것을 권장합니다.

- **Kimi**: https://platform.moonshot.cn/ Moonshot AI의 Kimi 시리즈로, 긴 컨텍스트와 Agent 역량이 뛰어납니다.
- **Zhipu GLM**: https://open.bigmodel.cn/ Zhipu AI의 GLM 시리즈(GLM-4.6 등)로, 중국어 역량과 비용 효율이 뛰어나 적극 권장합니다.
- **Siliconflow**: https://siliconflow.cn/ DeepSeek, Qwen 등 여러 오픈 소스 모델을 제공합니다.
- **Volcengine**: https://www.volcengine.com/product/ark ByteDance의 비공개 모델(Doubao)을 제공하며 중국 내 접속 지연 시간이 짧습니다.
- **OpenRouter**: https://openrouter.ai/ 중국 본토에서 Gemini 2.5 Pro, Claude 4 Sonnet, OpenAI GPT-5 등 여러 해외 비공개 및 오픈 소스 모델에 접근할 수 있습니다. 공식 API에는 해외 IP와 결제 수단이 필요하고, OpenAI는 해외 신원 확인도 요구하여 가입이 더 번거롭습니다.

모델 선택은 다음 글을 참고하세요: https://01.me/2025/07/llm-api-setup/

## 📦 부록 · 외부 저장소 가져오기

크기와 저작권 문제로 6·7·9장에서 사용하는 평가 벤치마크와 학습 프레임워크는 이 저장소에 **포함되어 있지 않습니다**. 아래에는 이 책에서 검증한 업스트림 주소와 커밋을 제시합니다. 각 저장소를 해당 디렉터리에 직접 복제해야 합니다. 다음 명령을 스크립트로 저장해 한 번에 받을 수도 있습니다.

```bash
# 6장 · 평가 벤치마크
git clone https://github.com/google-research/android_world.git         chapter6/android_world
git clone https://huggingface.co/datasets/gaia-benchmark/GAIA          chapter6/GAIA
git clone https://github.com/xlang-ai/OSWorld.git                      chapter6/OSWorld
git clone https://github.com/SWE-bench/SWE-bench.git                   chapter6/SWE-bench
git clone https://github.com/sierra-research/tau2-bench.git            chapter6/tau2-bench
git clone https://github.com/laude-institute/terminal-bench.git        chapter6/terminal-bench

# 7장 · 학습 프레임워크(bojieli/*는 이 책에 맞게 수정한 브랜치)
git clone https://github.com/bojieli/minimind.git                      chapter7/MiniMind-pretrain/minimind      # 실험 7-3 LLM 처음부터 학습
git clone https://github.com/bojieli/minimind-v.git                    chapter7/MiniMind-pretrain/minimind-v    # 실험 7-4 VLM 처음부터 학습(프로젝션 계층)
git clone https://github.com/bojieli/AdaptThink.git                    chapter7/AdaptThink-original
git clone https://github.com/bojieli/AWorld.git                        chapter7/AWorld
git clone https://github.com/bojieli/SFTvsRL.git                       chapter7/SFTvsRL
git clone https://github.com/bojieli/verl.git                          chapter7/verl
git clone https://github.com/thinking-machines-lab/tinker-cookbook.git chapter7/tinker-cookbook
git clone https://github.com/bojieli/lighteval.git                     chapter7/Intuitor/lighteval
git clone https://github.com/19PINE-AI/rlvp.git                        chapter7/RLVP/rlvp                       # 실험 7-14 RLVP 논문 코드
git clone https://github.com/PRIME-RL/SimpleVLA-RL.git                 chapter7/SimpleVLA-RL/SimpleVLA-RL       # 실험 7-13 시각·언어·행동 RL

# 9장 · 브라우저 자동화 및 Claude 예제
git clone https://github.com/browser-use/browser-use.git               chapter9/browser-use
git clone https://github.com/anthropics/claude-quickstarts.git         chapter9/claude-quickstarts

# 10장 · 이중 Agent 아키텍처(현재 독립 TalkAct 프로젝트) + Stanford AI Town
git clone https://github.com/19PINE-AI/TalkAct.git                     chapter10/use-computer-while-calling
git clone https://github.com/joonspk-research/generative_agents.git    chapter10/generative_agents             # 실험 10-7 Stanford AI Town
```

> 프로젝트 README에서 특정 커밋을 지정한 경우 재현 가능한 결과를 위해 해당 버전으로 `git checkout`하세요.
> 10장의 `use-computer-while-calling` 디렉터리는 독립적으로 유지 관리되는 [19PINE-AI/TalkAct](https://github.com/19PINE-AI/TalkAct) 저장소로 발전했습니다. 이 저장소에는 안내 문서(`chapter10/use-computer-while-calling/README.md`)만 남아 있습니다.

**실제 하드웨어/외부 환경이 필요한 실험(이 저장소에는 코드가 없으므로 업스트림 문서 참고):**

- **실험 9-8 / 9-9 · XLeRobot 원격 조작 및 LLM Agent 제어**: SO-100/XLeRobot 로봇 팔이 필요합니다. 업스트림 문서를 따르세요 — [Teleop](https://xlerobot.readthedocs.io/en/latest/software/getting_started/XLeRobot_teleop.html) · [LLM Agent](https://xlerobot.readthedocs.io/en/latest/software/getting_started/LLM_agent.html)
- **실험 9-10 · RGB Zero-Shot Sim2Real 파지**: [`StoneT2000/lerobot-sim2real`](https://github.com/StoneT2000/lerobot-sim2real)(시뮬레이션 학습은 GPU만으로 가능하며 실제 배포에는 SO-100 로봇 팔이 필요합니다.)
- **실험 6-11 · OpenVLA + RoboTwin2 시뮬레이션 평가**: VLA 학습/환경 의존성은 `chapter7/SimpleVLA-RL`의 README에 설명되어 있습니다(OpenVLA와 RoboTwin2를 가져와 설정하는 방법 포함).

**독자 실습(책에서 연습 문제로 제시하며, 전용 디렉터리 없이 기존 문서화 프로젝트 재사용):**

- **실험 5-12 · Agent를 만드는 Agent**: `chapter5/coding-agent`를 기반으로 부트스트래핑 방식으로 확장
- **실험 6-2 / 6-3 / 6-4 / 6-9**: 인간 기준선, 메모리 평가, JSON Cards와 RAG 비교, 메모리 선택 — 3장의 `user-memory` / `user-memory-evaluation` / `contextual-retrieval` 프로젝트를 응용
- **실험 7-8 · 프롬프트 증류**: 8장의 `chapter8/prompt-distillation`에 구현(장 간 재사용)
- **실험 7-9 · CoT 증류 `[확장]`**: 책에서 독자 확장 연습을 위한 실험 설계와 인수 기준을 제공하며 아직 전용 코드는 없습니다.

## 🤝 기여

이 책과 실습 코드는 모두 오픈 소스입니다. 커뮤니티 협업을 위한 Pull Request를 환영합니다. 특히 다음과 같은 기여에 감사드립니다.

1. **책 내용 개선**: 오류 수정, 내용 보충, 더 명확한 설명, 최신 발전 내용 추가(중국어 원문은 `book/chapter*.md`, 영어 번역은 `book-en/chapter*.md`)
2. **코드 개선 및 버그 수정**: 실습 프로젝트를 더 견고하고 사용하기 쉬우며 프로덕션 환경에 가깝게 개선
3. **새로운 실습 프로젝트**: 실험 구현을 보완·대체하거나 완전히 새로운 예제 프로젝트 기여
4. **책 삽화 디자인 개선**: `book/images/`(중국어)와 `book-en/images/`(영어)의 다이어그램을 더 명확하고 보기 좋게 개선(삽화는 각 디렉터리의 `gen_*_figs.py`로 생성)

제출하기 전에 관련 실험을 직접 실행해 재현 가능성을 확인하는 것을 권장합니다. 먼저 Issue를 열어 아이디어를 논의해도 좋습니다.

## 📄 라이선스

이 프로젝트는 [Apache License 2.0](LICENSE)에 따라 배포됩니다. 자세한 내용은 [`LICENSE`](LICENSE) 파일을 참고하세요. 일부 하위 프로젝트에는 별도 라이선스 정보가 있을 수 있으므로 해당 프로젝트의 안내를 확인하세요.

## ⭐ Star 기록

<a href="https://star-history.com/#bojieli/ai-agent-book&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/star-history-dark.png" />
    <source media="(prefers-color-scheme: light)" srcset="assets/star-history-light.png" />
    <img alt="Star 기록 차트" src="assets/star-history-light.png" width="720" />
  </picture>
</a>

<sub>이 차트는 [`scripts/gen_star_history.py`](scripts/gen_star_history.py)로 작성되었으며(2026년 7월 13일부터), [GitHub Actions 예약 작업](.github/workflows/star-history.yml)이 매일 새로 고쳐 <code>assets/</code> 디렉터리에 커밋합니다. 차트를 클릭하면 star-history.com에서 실시간 데이터를 볼 수 있습니다.</sub>
