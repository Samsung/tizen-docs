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

## v1.2.0 변경 사항 (2026-10-25)

tizen-agent-skills v1.2.0은 `tizen-sdk-skills` 1.5.0과 `tizen-action-skills` 1.0.0을 포함하는 다섯 번째 통합 릴리스입니다. 새 스킬은 없으며, 여러 Tizen 플랫폼 버전을 나란히 관리할 수 있게 되었고, Wayland/HWC 타겟용 스크린샷 폴백과 dlog-analyzer `crash-report` 액션이 추가되었으며, SDK·TV SDK·플랫폼 설치 관련 수정이 포함됩니다.

### tizen-sdk-skills 플러그인
- 플러그인 버전 1.4.5 → 1.5.0으로 상향
- Tizen AI Extension(vsix) 1.5.0 및 독립 실행형 CLI 번들 `tizen-sdk-v1.5.0.zip` 동반 릴리스

### 여러 플랫폼 버전 관리
- `platform-install --list`(tizen-cli `platform-list`, 새 읽기 전용 명령)가 각 `platforms/tizen-X.Y`를 `installed`, `incomplete`(완료되지 않은 `platform-install`), `not_installed`로 보고하며, 프로필과 에뮬레이터 이미지, 가장 높은 설치 버전을 함께 표시
- `create`와 `list-templates`가 `--platform-version <X.Y>`를 지원. 설치되지 않은 버전은 `platform_version_not_found`로 실패하며 `platform-install` 명령을 안내. 옵션이 없으면 가장 높은 설치 플랫폼을 사용. 기존에는 공유 `common` 데이터만 있는 버전을 선택할 수 있었음
- `--type tv`에서 버전을 지정하면 해당 `tv-samsung-X.Y` 프로필도 선택하며, 그 TV 확장이 없으면 TV 확장이 있는 버전을 안내하며 실패

### Wayland/HWC 타겟용 스크린샷 폴백
- DA 가전처럼 HWC가 UI를 오버레이 플레인에 올려 디바이스 덤프가 검은 화면으로 나오던 타겟에서, `enlightenment_info` 단계가 `winfo`로 배포된 클라이언트도 찾고 단색 덤프는 HWC를 끈 상태로 한 번 재시도한 뒤 HWC를 복원
- 모든 디바이스 측 방법 이후에 호스트 측 VNC 폴백이 실행됨. sdb로 디바이스의 5900 포트를 포워딩하거나 `TIZEN_VNC_SERVER`를 사용하며, 클라이언트는 모든 호스트의 vncdotool 또는 Linux의 `vncsnapshot`. 스크립트 타임아웃이 60초에서 90초로 늘었고, 엔벨로프 경고가 설치할 항목이나 VNC 연결 실패 원인을 안내

### dlog-analyzer 크래시 리포트
- 새 `crash-report` 액션이 `/opt/usr/share/crash/dump`, `/run/crash/dump`, `--dump-dir`의 crash-worker 덤프를 조회하고 앱 ID 또는 프로세스 이름(`--process`)으로 매칭하므로, 앱 ID가 없는 시스템 데몬도 다룰 수 있음. 최신 덤프(`--limit`, 기본값 3)의 시그널, 실행 파일, 콜 스택을 반환하고 `.info` 리포트와 함께 묶인 dlog를 저장하며 해당 `error-analyze` 호출을 제시. 읽을 수 있는 덤프 디렉터리가 없으면 `permission_denied`로 실패하며 `root on`을 안내

### 수정 사항
- `create`, `list-templates --type tv --platform-version X.Y`의 TV 안내가 `tizen-tv-sdk-install`과 `tizen-tv-sdk-install-from-zip`을 모두 제시하므로, 온라인 저장소에 없는 버전의 TV 확장도 ZIP으로 설치 가능. TV SDK가 이미 설치로 표시된 경우 `--force`를 추가
- 플랫폼 버전은 `platforms/tizen-X.Y`에 실제 플랫폼 콘텐츠가 있고 진행 중 마커가 남아 있지 않을 때만 설치된 것으로 판정. `tizen-platform-install`이 이미 있는 버전을 다시 내려받지 않고, `--force`가 다른 버전의 기록을 지우지 않으며, 실패한 실행은 완료로 간주되지 않고 이어서 재개됨
- Cline에서 TV SDK 설치가 동작: 스킬이 사용하던 `--detach`, `--status` 옵션을 설치 프로그램에 추가하고, Cline 실행 명령이 `--force`(Windows에서는 `-ZipPath`도)를 유지하며, Linux 폴러가 실행 중인 설치가 없을 때 `STATUS=running`을 보고하지 않고, Windows 분리 실행이 공백이 포함된 경로를 따옴표로 감쌈
- `--force` / `-Force`가 매니페스트가 있는 패키지를 모두 건너뛰지 않고 설치된 SDK를 실제로 재설치하므로, 새 패키지와 `--repo-url` 전환이 반영됨. 중간에 실패한 강제 실행은 더 이상 설치 완료로 보고되지 않음
- SDK 및 TV SDK 설치 스킬이 Cline 설치 실패를 포함한 모든 완료 경로에서 결과 엔벨로프를 보고

---

## v1.1.2 변경 사항 (2026-10-21)

tizen-agent-skills v1.1.2는 `tizen-sdk-skills` 1.4.5와 `tizen-action-skills` 1.0.0을 포함하는 네 번째 통합 릴리스입니다. 새 스킬은 없으며, 명령 가드 훅이 Tizen 작업으로 범위가 한정되고, Platform(GBS) 빌드가 ARM 디바이스를 겨냥할 수 있게 되었으며, 에뮬레이터·디버그·설치 관련 수정이 포함됩니다.

### tizen-sdk-skills 플러그인
- 플러그인 버전 1.4.4 → 1.4.5로 상향
- Tizen AI Extension(vsix) 1.4.5 및 독립 실행형 CLI 번들 `tizen-sdk-v1.4.5.zip` 동반 릴리스

### 명령 가드 훅
- 훅이 Tizen 작업으로 범위가 한정됨: Tizen 도구 규칙(tz 플래그, sdb 경로, gdbserver, em-cli, dlog 프로브, 타이머 대기)은 플러그인을 통해 SDK가 구성된 경우(`~/.tizen.sdk.path.config` 존재)에만 적용. 해당 파일이 없는 프로젝트에서는 호스트 셸 문법 규칙만 유지되므로 `which sdb`, `tizen version` 같은 일반 환경 확인이 더 이상 차단되지 않음
- Tizen Studio의 `tizen` CLI와 sdb 위치 확인(`which` / `where` / `Get-Command sdb`)을 더 이상 금지하지 않음
- 직접 입력한 sdb는 구성된 SDK의 `tools/sdb`여야 함. 다른 디렉터리의 sdb(두 번째 SDK 설치본, `tools/tizen-core/`, 복사본)는 구성된 경로와 `tizen-sdk-init`을 안내하는 메시지와 함께 거부

### Platform(GBS) 빌드
- `tizen-build-project`가 ARM 디바이스를 대상으로 할 수 있음. 요청을 `--arch x86_64`(에뮬레이터), `armv7l`(32비트 ARM), `aarch64`(64비트 ARM)로 매핑하고, 아키텍처가 지정되지 않은 디바이스 빌드에서는 묻는 흐름 추가. 디바이스의 `uname -m`과 `/usr/lib64` 존재 여부로 아키텍처를 판별. 기존에는 Platform 빌드가 항상 에뮬레이터 전용 x86_64 RPM을 생성

### 수정 사항
- `launch-emulator --timeout 0`이 실패 대신 300초 대기하던 문제 수정. `--timeout`이 없을 때만 300초 기본값을 사용하며, `0`은 1–540 범위 밖 값처럼 `invalid_parameters`로 거부
- `emulator-manager modify --size`가 `--platform` 없이 호출될 때 잘못된 템플릿 목록으로 크기를 해석하던 문제 수정. 이제 `list-vm --detail`로 VM의 플랫폼을 조회해 해당 플랫폼의 템플릿을 사용
- `tizen-gdb-debug`가 빈 `GDB init file:` 마커를 받아들이던 문제 수정. 빈 마커는 더 이상 성공으로 보고하지 않음
- `tizen-dotnet-debug`가 "package … not found" 출력을 모두 netcoredbg 누락으로 분류하던 문제 수정. netcoredbg 관련 출력만 해당 방식으로 분류
- `tizen-playwright-test`의 `--port`, `--setup-timeout`, `--timeout`이 `9222abc`, `1.9`, `30s` 같은 부분 숫자를 받아들이던 문제 수정. 이제 정수만 허용
- `tizen-install-app`, `tizen-playwright-test`, 프로젝트 생성·삭제·빌드·템플릿 조회, 삼성 인증서 플로우의 초기 검증 실패 시 `duration_ms`가 호출 시점부터 측정되도록 수정

### 내부 개선
- 에뮬레이터, 디버그, install-app, playwright-test, dlog-analyzer, sdb-helper, 삼성 인증서 모듈을 모듈 전용 헬퍼로 분리해 순환 복잡도를 낮춤. 동작 변화 없음: 내보내는 API, 엔벨로프, 메시지, 오류 코드는 모두 동일
- 저장소에 PR 검사(`check-pr.js`)와 이를 활용해 `tizen-sdk-skills` PR을 리뷰하는 에이전트 스킬이 추가됨

---

## v1.1.1 변경 사항 (2026-10-18)

tizen-agent-skills v1.1.1은 `tizen-sdk-skills` 1.4.4와 `tizen-action-skills` 1.0.0을 포함하는 세 번째 통합 릴리스입니다. 새 스킬은 없으며, 기존 스킬의 기능 추가와 라우팅 및 에뮬레이터 관련 수정이 포함됩니다.

### tizen-sdk-skills 플러그인
- 플러그인 버전 1.4.3 → 1.4.4로 상향
- Tizen AI Extension(vsix) 1.4.4 및 독립 실행형 CLI 번들 `tizen-sdk-v1.4.4.zip` 동반 릴리스

### tizen-dlog-analyzer
- 러너가 번들된 v0.2.8a0 분석기 바이너리의 기능 세트를 제공 (바이너리 자체는 v1.1.0과 동일)
- 새 `rules` 액션: `rules list` / `rules show <id>` / `rules validate [path]` / `rules test <fixture.json>`으로 내장 분석 규칙 24개를 읽기 전용으로 조회. `--rules-dir <path>`로 사용자 규칙 YAML 추가 로드
- `investigate`에 v0.2.8a0 옵션 추가 (`--rules-dir`, `--parallel`, `--max-workers`, `--deduplicate`, `--similarity-threshold`, `--allow-heavy`, `--no-noise-filter`, `--fuzzy-symptoms`, `--symptom-map`). 결과에 순위가 매겨진 `conclusions`(신뢰도, 역할, 근거, 수정), `ruled_out`, `unexplained`, `consent_needed`, `redaction_summary` 포함
- `probe run`에 앱 범위를 지정하는 `--app-id`와 사용자 동의 시에만 네트워크 프로브를 실행하는 `--allow-network-probe` 옵션 추가
- 기존 캡처 파일을 오프라인으로 분석하는 파일 모드 지원
- 분석 보고서 템플릿의 근본 원인 항목에 `Confidence`/`Role` 필드, `Ruled Out` 및 `Unexplained Anomalies` 섹션 추가
- 새 가드 규칙이 `sdb shell`에서 직접 입력한 `openssl s_client` / `curl` / `wget`을 거부하고, 동의 기반 `--allow-network-probe` 옵션을 안내

### 에뮬레이터 관리
- "사용 가능한 에뮬레이터 목록" 같은 요청이 `tizen-create-emulator`의 `list-vm --detail`로 라우팅되어, 어시스턴트가 VM을 직접 찾아 나서지 않음. 새 가드 규칙이 `em-cli` 직접 실행과 에뮬레이터 VM 디렉터리에 대한 `ls` / `find` / `Get-ChildItem`을 차단
- `list-vm --detail`이 플랫폼 이미지 이름에서 파생한 각 VM의 `profile`을 보고 (`tizen-*` → `tizen`, `tv-*` → `tv`). `tizen-10.0-x86_64` VM이 더 이상 Mobile 에뮬레이터로 표시되지 않음
- VM 이름을 지정하지 않으면 `tizen-launch-emulator`가 플랫폼 버전을 구간별로 비교하고 프로필로 필터링하여, `10.0`이 `9.0`보다 우선 선택되고 `tizen` 요청이 TV 이미지를 고르지 않음
- WSL용 에뮬레이터 홈 화면 복구가 헤드리스 Linux 호스트에도 적용됨

### 러너 탐색
- 모든 SKILL.md의 CLI 러너 탐색 섹션에 `node` 줄을 그대로 실행하라는 안내 추가

### 테스트 러너
- 플러그인 테스트 러너가 `PATH`의 전역 설치 `tizen-cli`/`tizen-sdk` 바이너리(오래된 설치일 수 있음)를 찾지 않고 항상 로컬로 빌드한 `tizen-sdk` 런처를 실행

---

## v1.1.0 변경 사항 (2026-10-14)

tizen-agent-skills v1.1.0은 `tizen-sdk-skills` 1.4.3과 `tizen-action-skills` 1.0.0을 포함하는 두 번째 통합 릴리스입니다. 새 스킬은 없으며, 아래 수정 및 개선이 포함됩니다.

### tizen-sdk-skills 플러그인
- 플러그인 버전 1.4.2 → 1.4.3으로 상향
- Tizen AI Extension(vsix) 1.4.3 동반 릴리스

### tizen-dlog-analyzer
- 번들 분석기 바이너리를 v0.2.8a0으로 갱신 (Linux / Windows / macOS)

### PowerShell 러너 탐색 개선
- 모든 SKILL.md의 PowerShell 러너 탐색 블록에 `FullName` 2차 정렬 키 추가: `powershell -Command "..."` 로 감싸서 실행할 때 외부 셸이 `$_` 를 빈 문자열로 전개하여 `[version]` 정렬이 무효화되는 문제를 완화
- 같은 자릿수 버전(1.4.0 vs 1.4.2)에서는 올바른 최신 버전을 선택하지만, 자릿수가 다른 버전(1.4.2 vs 1.4.10)에서는 더 낮은 버전을 고를 수 있으므로 래퍼 감싸기 사용은 여전히 권장하지 않음
- 가드 규칙에 이 완화책의 한계를 명시

### 리포지토리 문서
- AI 코딩 에이전트를 위한 리포지토리 수준 `AGENTS.md` 추가: 플러그인 구조, 버전 관리 모델, 문서 규칙, 보안, 커밋/PR 스타일, 플러그인별 검증 명령을 포함

---

## v1.0.0 변경 사항 (2026-10-07)

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
