# Git Flow

### Git Flow

- Git을 활용하여 협업하는 흐름으로 브랜치를 활용하는 전략을 말함

- Git을 CLI에서 활용하기 위해서는 `$ git status`는 필수적이므로 항상 모든 명령어 뒤에 상태를 확인해야 함

- GitHub Flow, GitLab Flow 등 각 서비스 별로 제안되는 서로 다른 흐름이 존재하므로 정해진 답은 없음

- 가장 대표적으로 활용되는 전략 :

  ![](03_flow.assets/git_flow.png)
  
  | branch        | feature | e.g. |
  | ------------- | ------- | ---- |
  | master (main)                 | 배포 가능한 상태의 코드                                      | LOL 클라이언트 라이브 버전  |
  | develop (main)                | 1) feature branch로 나뉘어지거나 발생된 버그 수정 등 개발 진행 2) 개발 이후 release branch로 갈라짐 | 다음패치를 위한 개발 (9.24) |
  | feature branches (supporting) | 1) 기능별 개발 브랜치(topic branch) 2) 기능이 반영되거나 드랍되는 경우 브랜치를 삭제함 | 기능별 업데이트             |
  | release branches (supporting) | 개발 완료 이후 QA/Test 등을 통해 얻어진 다음 배포 전 minor bug fix 등을 반영 | 9.24a, 9.24b 등             |
  | hotfixes (supporting)         | 1) 긴급하게 반영해야 하는 bug fix 2) release branch는 다음 버전을 위한 것이라면 hotfix branch는 현재 버전을 위한 것 | 긴급 패치를 위한 작업       |
  

ㅤ

### Branch

#### 1. 기본 명령어

| 명령어 | 내용 |
| ------ | ---- |
| (master) $ git branch *branch name*      | 브랜치 생성         |
| (master) $ git checkout *branch name*    | 브랜치 이동         |
| (master) $ git checkout -b *branch name* | 브랜치 생성 및 이동 |
| (master) $ git branch                    | 브랜치 목록         |
| (master) $ git branch -d *branch name*   | 브랜치 삭제         |
| (master) $ git merge *branch name*       | 브랜치 병합         |

ㅤ

#### 2. 명령어 [`merge`](https://victorydntmd.tistory.com/78)

- 각 브랜치에서 작업을 한 이후 이력(커밋)을 합치기 위해서는 일반적으로 merge를 사용함
- 병합을 진행할 때, 만약 서로 다른 이력에서 동일한 파일을 수정한 경우 충돌이 발생할 수 있음
  - 반드시 직접 수정을 진행해야 함
  - 오류가 발생한 것이 아니라 이력이 변경되는 과정에서 반드시 발생할 수 있는 것
- Fast-forward : 기존 master 브랜치에 변경 사항이 없어서 단순히 앞으로 이동함
  - feature *sub-branch name*으로 이동 후 commit
  - master에 별도의 변경이 없음
  - master 브랜치로 병합함
- Merge Commit : 기존 master 브랜치에 변경 사항이 있어서 병합 커밋이 발생함
  - feature *sub-branch name*으로 이동 후 commit
  - master 브랜치 commit
  - master 브랜치로 병합함

ㅤ

ㅤ

# GitHub Flow

### 기본 원칙

- GitHub Flow는 GitHub에서 제안하는 브랜치 전략으로 다음과 같은 기본 원칙을 가지고 있음

  1. master 브랜치는 반드시 배포 가능한 상태여야 한다.

  2. feature 브랜치는 각 기능의 의도를 알 수 있도록 작성한다.

  3. **Commit Message는 매우 중요하며, 명확하게 작성한다.**

  4. Pull Request를 통해 협업을 진행한다.

  5. 변경사항을 반영하고 싶다면, master 브랜치에 병합한다.

  > 1. There's only one rule: anything in the master branch is always deployable.
  >
  > 2. Your branch name should be descriptive, so that others can see what is being worked on.
  >
  > 3. Commit messages are important. By writing clear commit messages, you can make it easier for other people to follow along and provide feedback.
  >
  > 4. Pull Requests are useful for contributing to open source projects and for managing changes to shared repositories.
  >
  > 5. Now that your changes have been vertified in production, it is time to merge your code into the master branch.

ㅤ

### GitHub Flow Models

#### 1. Feature Branch Workflow

- Shared Repository Model (저장소의 소유권이 **있는** 경우)

1. 각 사용자는 원격 저장소의 소유권을 가진 상태(master)이므로 clone을 통해 저장소를 로컬에 복제함
2. 기능 추가를 위해 각자 브랜치를 생성하고 기능을 구현함
3. 기능을 구현한 후 원격 저장소에 각자의 브랜치를 반영함 (개별적 push)
4. 원격 저장소에서 Pull Request를 통해 merge 함
5. 병합이 완료된 브랜치를 삭제함
6. 각자 master 브랜치로 switch 후 병합된 master의 내용을 pull 함
7. 원격 저장소에서 병합 완료 된 로컬 브랜치는 삭제함
8. 새로운 기능 추가를 위해 위의 과정을 반복함

ㅤ

#### 2. Forking Workflow

- Fork & Pull Model (저장소의 소유권이 **없는** 경우)

1. 소유권이 없는 원격 저장소를 fork를 통해 clone 함

2. 추후 로컬 저장소를 원본 원격 저장소와 동기화를 하기 위해 url을 연결함

   `$ git remote add upstream 원본주소`

3. 기능 추가를 위해 브랜치를 생성하고 기능을 구현함

4. 기능을 구현 후 원격 저장소에 브랜치를 반영함 (push)

5. 원본 원격 저장소에 Pull Request를 보냄

6. 원본 원격 저장소에서 병합이 완료되면

7. 자신의 원격 저장소에 있던 병합 완료된 브랜치는 삭제함

8. master 브랜치로 switch

9. 병합된 master의 내용을 원본 원격 저장소로부터 pull 함

   `$ git pull upstream master`

10. 원격 저장소에서 병합 완료된 로컬 브랜치는 삭제함

11. 새로운 기능 추가를 위해 위의 과정을 반복함

ㅤ

#### 3. 참고 사이트

- [GitHub Docs](https://guides.github.com/)