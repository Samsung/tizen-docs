# Tizen Agent Skills 에이전트 요약

## 개요
Tizen Agent Skills는 AI 에이전트를 위한 전문 기능 모음으로, Tizen 개발 환경에서 다양한 작업을 자동화하고 지원합니다.

---

## 핵심 에이전트별 기능

### 1. dlog-analyzer (로그 분석기)
**주요 기능:**
- 증상 조사 흐름: investigate, probe, kernel collect/analyze, snapshot, timeline
- 문제 보고서 라우팅 (device-manager와 분리)
- 사용자 중심 재현 윈도우
- SDK 데이터 디렉토리에 로그 저장
- macOS 분석기 바이너리 지원

**사용 시기:** Tizen 장치/에뮬레이터 문제 조사 및 로그 분석

---

### 2. dotnet-setup (.NET 환경 설정)
**주요 기능:**
- 위치별 SDK 선택
- `--dotnet-root` / `--persist-env` 옵션 지원
- 현재 실행을 위한 번들 dotnet 사용

**사용 시기:** .NET 개발 환경 초기 설정

---

### 3. dotnet-debug (.NET 디버깅)
**주요 기능:**
- `.vscode/launch.json` 및 `tasks.json` 자동 생성
- relaunch preLaunchTask 지원

**사용 시기:** Tizen .NET 앱 원격 디버깅

---

### 4. sdk-install (SDK 설치)
**주요 기능:**
- UTC+9 호스트에서 download.tizen.org 사용
- Cline 분리 설치 (최대 4회 폴링)

**사용 시기:** Tizen SDK 초기 설치 및 구성

---

### 5. create-project (프로젝트 생성)
**주요 기능:**
- 10자 ASCII 문자/숫자 앱 이름 규칙
- `--force` 검증 순서 처리
- tizen-11.0 매니페스트 API 버전 수정
- 유효한 이름 예제 제공

**사용 시기:** 새로운 Tizen 앱 프로젝트 생성

---

### 6. sdb-helper / device-manager / file-transfer
**주요 기능:**
- 앱 언설치 지원
- stop + launch를 통한 에뮬레이터 재시작
- kernel-log 핸드오프
- 패키지 ID 처리
- MSYS 원격 경로 복원
- 여러 장치 동시 처리

**사용 시기:** 장치/에뮬레이터 관리, 파일 전송, 앱 제어

---

### 7. Standalone CLI (독립 실행형 CLI)
**주요 기능:**
- `--help`/`--version`에 JSON 인벨로프 지원
- `--schema` 민감한 플래그
- `TIZEN_SDK_INLINE_INSTALLER` 환경 변수

**사용 시기:** 명령줄 기반 자동화 및 스크립팅

---

## 주요 개선사항

| 항목 | 설명 |
|------|------|
| **로그 분석** | 상세한 증상 조사 및 kernel 레벨 분석 |
| **개발 환경** | .NET 워크로드 및 SDK 자동 관리 |
| **프로젝트 생성** | 명확한 규칙과 검증 로직 |
| **장치 관리** | 다중 장치 동시 지원 |
| **자동화** | CLI 기반 완전 자동화 가능 |

---

## 활용 시나리오

1. **신규 개발 환경 구성**
   - sdk-install → dotnet-setup → create-project

2. **앱 개발 및 테스트**
   - create-project → 코딩 → build → install-app

3. **문제 해결**
   - dlog-analyzer를 통한 로그 수집 및 분석

4. **배포 자동화**
   - CLI를 통한 스크립트 기반 빌드 및 설치

---

## v1.0.0 변경 사항 (2026-10-01)

tizen-agent-skills PR #26으로 반영된 패치 릴리스입니다. 새 스킬은 없고, 아래 수정이 포함됩니다.

### dlog-analyzer
- 번들 분석기 바이너리를 v0.2.5a0으로 갱신 (Linux / Windows / macOS)
- 수집기 락(`_meta/collector.lock`) 처리 수정: 다른 수집기가 락을 쥐고 있을 때 `start`가 성공으로 보고된 뒤 락 파일을 지우던 문제를 고치고, 이제 `already_running`과 함께 보유 PID 및 중지 명령을 반환. 러너는 락 파일을 절대 건드리지 않음
- 이전 세션의 수집기가 락을 보유한 경우, PID의 실행 파일 이름을 확인해 `tizen-dlog-analyzer`일 때만 종료를 안내하고, PID가 재사용된 경우에는 stale lock으로 보고
- 러너가 자기 플러그인 버전에 포함된 바이너리를 우선 사용하고, 캐시를 탐색할 때는 최신 버전을 선택 (이전에는 처음 발견한 디렉토리의 구버전 바이너리를 실행해 `investigate`가 `No such command`로 실패할 수 있었음)
- Windows cp949 코드 페이지에서 `UnicodeEncodeError`로 보고서가 잘리면, 트레이스백만 반환하지 않고 출력된 보고서를 `success` + 경고 + `output_truncated: true`로 반환

### Cline on Windows (PowerShell 터미널)
- SKILL.md의 러너 탐색 블록 제목이 셸을 명시 (cmd.exe 체인은 cmd.exe 전용, PowerShell 블록은 터미널에서 직접 실행)
- PowerShell `node "$CLI" …` 줄에 `$CLI` 비어 있음 가드 추가 (단독 실행 시 `Cannot find module '<cwd>\list-templates'` 같은 오해를 부르는 MODULE_NOT_FOUND 방지)
- 가드 규칙(한국어 7/9, 영어 8/10)에 두 가지 실패 양상을 명시하고, 인코딩 래퍼는 `$`가 없는 명령에만 사용하도록 제한

### 설치 스크립트
- `setup.ps1`이 `setup.sh` 표기(`--harness … --repo … --skip-validation --no-restart`)도 수용

---

## 참고사항

- 모든 에이전트는 상호 보완적으로 작동
- 로그 분석은 모든 문제 보고의 중심
- 다중 플랫폼(Windows, macOS) 지원
- Tizen 11.0 이상 매니페스트 호환성 보장
