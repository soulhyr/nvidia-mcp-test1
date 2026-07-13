# MCP 기업 관리 시스템 (Company Management System)

MCP(Model Context Protocol)를 활용하여 **사내 직원 정보**, **업무 할 일(Todo)**, 그리고 **사내 규정**을 통합 관리하는 지능형 시스템입니다.

## 📌 프로젝트 소개

본 프로젝트는 MCP(Model Context Protocol)를 기반으로 다음 기능을 제공합니다.

- 👤 직원 정보 저장 및 조회
- ✅ 업무(Todo) 생성 및 관리
- 📖 사내 규정(Resource) 조회 및 검색
- 🤖 AI 프롬프트를 활용한 규정 답변 및 인사 보고서 자동 생성

---

# 📂 프로젝트 구조

```text
.
├── data/               # 데이터 저장소 (employees/, todos/)
├── tools/              # MCP 기능 모듈
│   ├── employee.py     # 직원 정보 저장/검색 툴
│   ├── todo.py         # 할 일 관리(CRUD) 툴
│   ├── policy.py       # 규정 리소스 및 검색 로직
│   └── prompts.py      # AI 비서용 프롬프트 정의
├── server.py           # MCP 서버 실행 파일
├── client.py           # 기능 검증용 클라이언트 테스트 스크립트
├── reset.py            # 시스템 데이터 초기화 스크립트
└── README.md
```

---

# 🚀 주요 기능

## 👤 직원 관리

- 직원 프로필 저장
- 직원 정보 검색
- 직원 상세 정보 조회

### 예시

- 이름
- 부서
- 직책
- 연락처
- 이메일

---

## ✅ Todo 관리

직원의 업무를 생성하고 관리합니다.

### 지원 기능

- Todo 생성
- Todo 조회
- 담당자별 조회
- 상태별 조회
- 진행 상태 변경(CRUD)

---

## 📖 사내 규정 관리

`policy://` Resource를 이용하여 사내 규정을 제공합니다.

### 지원 기능

- 규정 조회
- 키워드 검색
- 규정 기반 답변 생성

---

## 🤖 AI 프롬프트

### Policy Expert

사내 규정을 근거로 답변을 생성합니다.

예시

> "연차는 몇 일까지 사용할 수 있나요?"

↓

관련 규정을 찾아 근거와 함께 답변

---

### Employee Summary

직원 정보를 기반으로 표준화된 인사 보고서를 생성합니다.

예시

- 직원 기본 정보
- 담당 업무
- 진행 중인 Todo
- 요약 보고서

---

# ⚙️ 설치

```bash
pip install mcp
```

---

# ▶️ 실행 방법

## 1. MCP 서버 실행

```bash
python server.py
```

---

## 2. 기능 테스트

클라이언트 시나리오를 실행합니다.

```bash
python client.py
```

테스트 내용

- 데이터 초기화
- 직원 저장
- 직원 조회
- Todo 추가
- Todo 조회

---

## 3. 데이터 초기화

```bash
python reset.py
```

---

# 🧪 테스트 시나리오

## 1. 시스템 초기화

- `reset.py` 실행
- `data/` 디렉터리가 초기화되는지 확인

---

## 2. 직원 정보 테스트

- `save_employee_info`
- `search_employee_info`

직원 정보가 정상적으로 저장 및 조회되는지 확인

---

## 3. Todo 관리 테스트

- `add_todo`
- `list_todos`

다음 기능을 검증합니다.

- 담당자별 조회
- 상태별 조회
- Todo 추가

---

## 4. AI 프롬프트 테스트

Claude Desktop(또는 MCP Client)에서 정의된 Prompt를 호출합니다.

### Policy Expert

- 규정을 기반으로 답변 생성

### Employee Summary

- 직원 정보 기반 보고서 생성

---

# 📁 데이터 저장 구조

```text
data/
├── employees/
│   └── *.json
└── todos/
    └── *.json
```

---

# 🛠 기술 스택

- Python
- MCP (Model Context Protocol)
- JSON 기반 데이터 저장

---

# 📄 라이선스
없어요~! 아무나 가져다 쓰시되 출처만 밝혀주세요~!