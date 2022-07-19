# Markdown

### 개요

- 2004년 존 그루버가 만든 텍스트 기반의 가벼운 [마크업 언어](https://ko.wikipedia.org/wiki/%EB%A7%88%ED%81%AC%EC%97%85_%EC%96%B8%EC%96%B4)

- 최초 마크다운에 비해 확장된 문법(표, 주석 등)이 있지만, 자료에서는 GitHub에서 사용 가능한 문법(GitHub Flavored Markdown)을 기준으로 설명함

  > Markdown is a **text-to-HTML conversion tool** for web writers.
  >
  > Markdown allows you to write using an **easy-to-read, easy-to-write plain text format**, then convert it to srtucturally valid XHTML (or HTML).
  >
  > ㅤ
  >
  > Thus, "Markdown" is two things:
  >
  > (1) **a plain text formatting syntax**
  >
  > (2) a software tool, written in Perl, **that converts the plain text formatting to HTML**.
  >
  > ㅤ
  >
  > The overriding **design goal for Markdown's formatting syntax is to make it as readable as possible**.

ㅤ

ㅤ

### 특징

- 단순한 텍스트 문법으로 내용을 작성하며, 다양한 환경에서 변환되어 보여짐
  - 다양한 문서 편집기(Text Editor), 웹 환경에서 모두 지원함
- 가급적 잘 읽을 수 있도록 최소한의 문법으로 구조화 됨
- 반면 워드프로세서(한글/MS Word)는 다양한 서식과 구조를 지원하며, 문서에 즉각적으로 반영 됨

ㅤ

ㅤ

### 활용 예시

#### 1. README.md

- GitHub 등의 사이트에서는 파일명이 README**.md**인 것을 모두 보여줌
- 오픈소스의 공식 문서를 작성하거나 개인 프로젝트의 프로젝트 소개서로 활용 됨
- 모든 페이지에 README.md를 넣어 문서를 바로 볼 수 있도록 활용 됨

ㅤ

#### 2. 기술 블로그

- 다양한 기술 블로그에서 [정적사이트생성기](https://www.daleseo.com/spa-ssg-ssr/#ssg-static-site-generator)(Static Site Generator)를 통해 활용함
- Jekyll, Gatsby, Hugo, Hexo 등을 통해 작성된 마크다운을 HTML, CSS, JS 파일 등으로 변환하고 GitHub Pages 기능을 통해 호스팅함(= 외부에 공개를 함)

ㅤ

#### 3. 기타

- 다양한 개발 환경 뿐만 아니라 일반 소프트웨어에서도 많이 사용되고 있음
- Jupyter Notebook에는 별도의 마크다운 셀이 있어 데이터 분석 등을 하는 과정에서 프로젝트 내용과 분석 결과를 정리할 수 있음
- Notion과 같은 메모/노트 필기 소프트웨어에서도 기본 문법으로 마크다운을 채택함

ㅤ

ㅤ

### 문법

#### 1. Heading

``` markdown
# h1 title
	.
	.
	.
# h6 title
```

- 문서의 제목이나 소제목으로 사용 됨
- #의 개수에 따라 대응되는 수준(Heading Level)이 있으며, h1~h6까지 표현 가능함
- 문서의 구조를 위해 작성 되며 글자 크기의 조절을 위해 사용되어서는 안 됨

ㅤ

#### 2. List

```markdown
1. ordered list
	- unordered list
	- unordered list
2. ordered list
			.
			.
			.
```

- 순서가 있는 리스트(ol)와 순서가 없는 리스트(ul)로 구성 됨

ㅤ

#### 3. Fenced Code Block

```markdown
​```markdown
```

- 백틱(backtick) 기호 3개를 활용하여 작성함

- 코드 블록에 특정 언어를 명시하면 구문 강조(Syntax Highlighting)가 적용 가능함

  (일부 환경에서는 적용 되지 않을 수 있음)

ㅤ

#### 4. Inline Code Block

```markdown
`markdown`
```

- 백틱(backtick) 기호 1개를 인라인에 활용하여 작성함

ㅤ

#### 5. Link

```markdown
[text](url)
```

- 특정 파일들을 포함해 연결시킬 수도 있음

ㅤ

#### 6. Image

```markdown
![alt](url)
```

- 특정 파일들을 포함해 연결시킬 수도 있음

ㅤ

#### 7. Blockquotes

```markdown
>quotes
```

ㅤ

#### 8. Table

```markdown
| Syntax    | Description |
| --------- | ----------- |
| Header    | Title       |
| Paragraph | Text        |
```

- 일부 지원이 안 되는 환경도 있음

ㅤ

#### 9. Text Emphasis

```markdown
you can use asterisks to make the texts **bold** and *italic*
or use underscores : __bold__, _italic_
```

- 굵게, 기울임을 통해 특정 글자들을 강조함

ㅤ

#### 10. Horizon

```markdown
***
---
___
```

- 3개 이상의 애스터리스크(asterisks), 대쉬(dashes)나 언더스코어(underscores)를 씀

ㅤ

ㅤ

### 관련 자료

- [GitHub Flavored Markdown](https://github.github.com/gfm/)
- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
- [Markdown Guide](https://www.markdownguide.org/)

ㅤ

ㅤ

### 개발자와 문서 작성

- [백엔드 개발자를 꿈꾸는 학생 개발자들에게](https://d2.naver.com/news/3435170) : 레벨 2 개발자 '자신이 경험한 사용법을 문서화해 팀 내에 전파할 수 있음'
- [Google Technical Writing](https://developers.google.com/tech-writing) : Every engineer is also a writer
- [Technical Writing Conference](https://engineering.linecorp.com/ko/blog/write-the-docs-prague-2018-recap/) : Clova 기술 문서 작성 및 관리 업무