# 원격 저장소 (Remote Repository)

### 정의

- 네트워크를 활용한 저장소
- GitHub, GitLab, Bitbucket 등



### 기본 흐름

- 로컬 저장소의 버전(커밋)을 원격저장소로 보내고, 원격 저장소의 버전(커밋)을 로컬 저장소로 가져옴



### 명령어

#### 1. 기본 명령어

| 명령어                          | 내용                   |
| ------------------------------- | ---------------------- |
| git clone *url*                 | 원격 저장소 복제       |
| git remote -v                   | 원격 저장소 정보 확인  |
| git remote add *원격저장소 url* | 원격 저장소 추가       |
| git remote rm *원격저장소*      | 원격 저장소 삭제       |
| git push *원격저장소 브랜치*    | 원격 저장소에 push     |
| git pull *원격저장소 브랜치*    | 원격 저장소로부터 pull |



#### 2. 명령어  `clone`

```bash
$ git clone (repository address)
```

- 원격 저장소를 복제해서 가져옴

- 원격 저장소 이름을 가진 폴더로 이동해서 활용함

- cf. 로컬에서 새로운 프로젝트를 시작할 때 : git init

  ​     원격에 있는 프로젝트를 시작할 때 : git clone



#### 3. 명령어  `remote add`

```bash
$ git remote add (origin) (repository address)
```

- 원격 저장소는 일반적으로 origin으로 설정함
- 원격 저장소 정보를 로컬 저장소에 추가함
- **로컬 저장소에는 한번만 설정해주면 됨**
- GitHub에서도 명령어를 확인할 수 있음



#### 4. 명령어  `push`

```bash
$ git push (origin) (master)
```

- 원격 저장소에 로컬 저장소 변경 사항(커밋)을 올림 (push)
- 로컬 폴더의 파일/폴더가 아닌 저장소의 **버전(커밋)이 올라감**
- push 할 때의 주의 사항 : 인증 정보가 필수적이므로 반드시 인증할 것



#### 5. 명령어  `pull`

```bash
$ git pull (orgin) (master)
```

- 원격 저장소로부터 변경된 내역을 받아와서 이력을 병합함



### 기타 주요 저장소 관리

#### 1. 저장소 이름 변경

- Settings > General > Repository Name
- **저장소 이름 변경 시 원격 저장소 url이 변경되므로 로컬 설정 변경이 필수적임**



#### 2. 저장소 Public / Private 전환 및 삭제

- Settings > General > Danger Zone



#### 3. 저장소 접근 관리

- Settings > Collaborators
- **저장소의 push 권한은 collaborator에게만 있음**
- 이메일로 초대를 받을 수 있으며, 승낙한 경우 공동 작업이 가능함



### Push 실패

- 로컬과 원격 저장소의 커밋 이력이 다른 경우 자주 발생함
  - 원격 저장소의 커밋을 로컬 저장소로 pull 해서
  - 로컬에서 두 커밋을 병합함 (추가 커밋 발생)
    - 동시에 같은 파일이 수정된 경우 Merge Conflict가 발생하나 브랜치 학습을 통해 해결이 가능함
  - 다시 GibtHub으로 push 함





# Git 파일 관리 심화

### .gitignore

- **이미 커밋된 파일은 반드시 삭제를 해야 .gitignore로 적용되므로 프로젝트 시작 전에 미리 설정하는 것을 권장함**
- 일반적인 개발 프로젝트에서 버전 관리를 별도로 하지 않는 파일/디렉토리가 발생함
- 일반적으로 [개발언어](https://github.com/github/gitignore), 개발환경이 있음
  - 파이썬(venv/), 자바스크립트(node_modules/)
  - 운영체제(windows, mac, linux), 텍스트 에티터/IDE(visual studio code 등)
- Git 저장소에 .gitignore 파일을 생성하고 해당 내용을 관리함
- 예시
  - 특정 파일 : a.txt (모든 a.txt), test/a.txt (테스트 폴더의 a.txt)
  - 특정 디렉토리 : /my_secret
  - 특정 확장자 : *.exe
  - 예외 처리 : !b.exe