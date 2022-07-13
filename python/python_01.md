# Computer Programming Language

- 의미
  - 컴퓨터(Computer) : Calculation + Remember
  - 프로그래밍(Programming) : 명령어의 모음(집합)
  - 언어 : 자신의 **생각을 나타내고 전달하기** 위해 사용하는 체계 **문법적**으로 맞는 말의 집합
- 컴퓨터에게 명령하기 위한 약속이며 명령적 지식(Imperative Knowledge)임





# Python 기초

### 장점

#### 1. Easy to learn

- 다른 프로그래밍 언어보다 문법이 간단하면서도 엄격하지 않음
  - 예 : 변수에 별도의 타입 지정이 필요 없음
- 문법 표현이 매우 간결하여 프로그래밍 경험이 없어도 짧은 시간 내에 마스터할 수 있음
  - 예 : 문장을 구분할 때 중괄호 대신 들여쓰기를 사용



#### 2. Expressive Language

- 같은 작업에 대해서도 C나 Java로 작성할 때 보다 더 간결하게 작성이 가능함

  ```c
  public class HelloPython {
      public static void main(String[] args) {
          System.out.println("Hello Python!");
      }
  }
  ```

  ```python
  print('Hello Python!')
  ```



#### 3. Cross Platform Programming Language

- 윈도우즈(Windows), macOS, 리눅스(Linux), 유닉스(Unix) 등 다양한 운영체제에서 실행 가능함



#### 4. <u>Interpreter</u>ed Language

- 소스코드를 기계어로 변환하는 컴파일 과정 없이 바로 실행이 가능함

- 코드를 대화하듯 한 줄 입력하고 실행한 후, 바로 확인할 수 있음

  ```python
  >>> 2 + 2 # 사용자가 입력 (input)
  4 # 컴퓨터가 대답 (output) 
  ```




#### 5. Object Oriented Programming

- Python은 [객체 지향 언어](https://gold-dragon.tistory.com/295)이며, 모든 것이 객체로 구현되어 있음
  - 객체(object) : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것



### 개발 환경

#### 1. IDLE (Intergrated Development and Learning Environment)

- Python의 기본 [인터프리터](https://ko.wikipedia.org/wiki/%EC%9D%B8%ED%84%B0%ED%94%84%EB%A6%AC%ED%84%B0)
- 내장 프로그램으로 Python 설치 시 기본적으로 설치가 되며, 인터프리터가 대화형 모드로 동작함
  - 여러 줄의 코드가 작성되는 경우 보조 프롬프트(...)가 사용 됨
  - 프롬프트( >>>)에 코드를 작성하면 해당 코드가 실행 됨
- Python이 설치된 환경에서는 기본적으로 활용 가능하나 디버깅 및 코드 편집, 반복 실행이 어려움



#### 2. Python 스크립트 실행

- IDE( Pycharm 등), Text Editor(Visual Studio Code 등) 등에서 작성한 Python 스크립트 파일을 직접 실행함



### 기초 문법

#### 1. Style Guide

- 코드를 '어떻게 작성할지'에 대한 가이드라인이 존재함
- Python에서 제안하는 스타일 가이드 : [PEP 8](https://www.python.org/dev/peps/pep-0008/ )
- 기업, 오픈소스 등에서 사용되는 스타일 가이드 : [Google Style guide](https://google.github.io/styleguide/pyguide.html) 등



#### 2. Identation (들여쓰기)

- 문장을 구분할 때 들여쓰기를 사용함
- 들여쓰기를 할 때는 'space키 4번' 혹은 'Tab키 1번'을 입력함
- **주의!** 한 코드 안에서는 반드시 한 종류의 들여쓰기를 사용해야 하며 혼용하면 안 됨 (Space Sensitive)
  - Tab으로 들여쓰면 계속 Tab으로 들여써야 함
  - 원칙적으로는 공백(빈칸, space) 사용을 권장함 (PEP 8 권장사항)



#### 3. Variable (변수)

- 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름

- 동일 변수에 언제든지 다른 객체를 할당할 수 있음(= 참조하는 객체가 바뀔 수 있음)

  - 같은 값을 동시에 할당할 수 있음
  - 다른 값을 동시에 할당 할 수 있음 (Multiple Assignment)

- 변수는 할당 연산자(=)를 통해 값을 할당 받음 (assignment)

- type() : 변수에 할당된 값(객체)의 타입

- id() : 변수에 할당된 값의 고유한 Identity 값, 메모리주소

- 예제

  ```python
  # x = 10 y = 20 일 때, 각각 값을 바꿔서 저장하는 코드를 작성하시오.
  x, y = 10, 20
  
  # 1 임시 변수 활용
  tmp = x
  x = y
  y = tmp
  print(x, y)
  
  # 2
  y, x = x, y
  print(x, y)
  ```



#### 4. Identifiers (식별자)

- Python 객체(변수, 함수, 모듈, 클래스 등)를 식별하는 데 사용하는 이름

- 규칙

  - 식별자의 이름은 영문 알파벳, 언더스코어, 숫자로 구성 됨

  - 첫 글자에 숫자가 올 수 없음

  - 길이 제한이 없으며, 대소문자를 구별함

  - 다음의 keywords는 예약어(Reserved Words)이므로 사용할 수 없음

    False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

  - 내장함수나 모듈 등의 이름으로도 만들면 안 됨

    - 기존 이름에 다른 값을 할당하게 되므로 더 이상 동작하지 않음

    ```python
    print(5)
    print = 'hi'
    print(5)
    
    # output
    TypeError Traceback (most recent call last)
    1 print(5)
    2 print = 'hi’
    ----> 3 print(5)
    TypeError: 'str' object is not callable
    ```



#### 5. Input (사용자 입력)

- input([prompt])
  - 사용자로부터 값을 즉시 입력 받을 수 있는 내장함수
  - 괄호 부분에 문자열을 넣으면 입력 시 해당 문자열을 출력할 수 있음
  - **반환값은 항상 문자열의 형태로 반환 됨**



#### 6. Comment (주석)

- 주석으로 처리 될 내용 앞에 ‘#’ 을 입력함
- 한 줄을 온전히 사용할 수도 있고, 그 줄 코드 뒷부분에 작성할 수도 있음
- 코드에 대해 설명하기 위해 사용 됨
  - 중요한 점이나 다시 확인해야 하는 부분을 표시함
  - 컴퓨터는 주석을 인식하지 않으며, 사용자만을 위한 것임
- 코드 이해에 도움을 주며, 코드의 분석 및 수정이 용이해짐 (→ 주석 작성은 개발자에게 중요한 습관임)
- 프로그램의 속도를 느리게 하지 않으며, 용량을 늘리지 않음





# Data Type (자료형)

### Boolean Type (불린형)

#### 1. Boolean

- True/False 값을 가짐
- 비교/논리 연산을 수행하는 데 활용 됨
- 다음은 모두 False로 변환 됨 : 0, 0.0, (), [], {}, '', None



#### 2. Logical Operator (논리 연산자)

- 논리식을 판단하여 참(True)과 거짓(False)을 반환함

  | 연산자  | 내용                           |
  | ------- | ------------------------------ |
  | A and B | A와 B 모두 True 시, True       |
  | A or B  | A와 B 모두 Flase 시, False     |
  | Not     | True를 False로, False를 True로 |



### Numeric Type (수치형)

#### 1. Int (Integer)

- 모든 정수 값
  - Python 3부터는 long 타입은 없고, 모두 int로 표기 됨
  - 여타 프로그래밍 언어, Python 2에서는 OS기준 32/64비트임
- 매우 큰 수를 나타낼 때 overflow가 발생하지 않음
  - overflow : 데이터 타입별로 사용할 수 있는 메모리의 크기를 넘어서는 상황
  - Arbitrary Precision Arithmetic(임의 정밀도 산술)을 통해 고정된 형태의 메모리가 아닌 가용 메모리들을 활용해 모든 수 표현에 이용함



#### 2. Float (Floating Point Number)

- 정수가 아닌 모든 실수 값

- [부동소수점](https://ko.wikipedia.org/wiki/%EB%B6%80%EB%8F%99%EC%86%8C%EC%88%98%EC%A0%90) 방식으로 표기함

  - [지수표기법](https://izen8.tistory.com/902)이 사용 됨

    ```python
    10 ** 100 / 3
    1 / -10 ** 100
    1e - 1
    
    # output
    3.333333333333333e+99
    -1e-100
    0.1
    ```



  - Floating Point Rounding Error가 발생함


    - 컴퓨터는 2진수(비트)로 숫자를 표현하는데 이 과정에서 발생하여 예상치 못한 결과가 나타나게 됨
    
    - 값을 비교하는 과정에서 정수가 아닌 실수일 경우 주의해야 함
    
    - 매우 작은 수보다 작은 지를 확인하거나 math 모듈을 활용해야 함
    
      ```python
      # 1 임의의 작은 수
      abs(a - b) <= 1e - 10
      
      # 2 math 모듈 활용
      import math
      math.isclose(a, b)
      ```



#### 3. Complex (Complex Number)

- 실수부와 허수부(j로 표현)로 구성된 복소수

  ```python
  a = 3 + 4j
  type(a)
  a.real
  a.imag
  
  # output
  class 'complex'
  3.0
  4.0
  ```



#### 4. Arithmetic Operator (산술 연산자)

- 기본적인 사칙연산 및 수식 계산

  | 연산자 |   내용   |
  | :----: | :------: |
  |   +    |   덧셈   |
  |   -    |   뺄셈   |
  |   *    |   곱셈   |
  |   **   | 거듭제곱 |
  |   /    |  나눗셈  |
  |   //   |    몫    |
  |   %    |  나머지  |



#### 5. In-place Operator (복합 연산자)

- 연산과 할당이 함께 이뤄짐

  | 연산자  |    내용    |
  | :-----: | :--------: |
  | a += b  | a = a + b  |
  | a -= b  | a = a - b  |
  | a *= b  | a = a * b  |
  | a **= b | a = a ** b |
  | a /= b  | a = a / b  |
  | a //= b | a = a // b |
  | a %= b  | a = a % b  |




#### 6. Comparison Operator (비교 연산자)

- 값을 비교하며 True/False 값을 리턴함

  |  연산자  |          내용          |
  | :------: | :--------------------: |
  |    <     |          미만          |
  |    <=    |          이하          |
  |    >     |          초과          |
  |    >=    |          이상          |
  |    ==    |          같음          |
  |    !=    |       같지 않음        |
  |   *is*   | *OPP(객체 아이덴티티)* |
  | *is not* |   *OPP가 아닌 경우*    |



### String Type (문자열)

#### 1. 특징

- 모든 문자
- 작은 따옴표나 큰 따옴표를 활용해 표기함
  - 문자열을 묶을 땐 동일한 문장부호를 활용해야 함
  - PEP 8에서는 소스코드 내에서 하나의 문장부호를 선택해 유지하도록 권고함

- 변경이 불가능(immutable)하나 반복이 가능(iterable)함



#### 2. 활용

- Escape Sequence : 문자열 내에서 특정 문자의 조작을 위해서 역슬래시를 활용해 구분함

- [String Interpolation](https://velog.io/@dyunge_100/%ED%8C%8C%EC%9D%B4%EC%8D%AC-format%EA%B3%BC-f-string%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC) : 변수를 활용해 문자열을 만드는 방식

  - %-formatting

    ```python
    name = 'Kim'
    score = 4.5
    
    print('Hello, %s' % name) # 문자열은 %s
    print('내 성적은 %d' % score) # 정수형은 %d
    print('내 성적은 %f' % score) # 실수형은 %f
    
    # output
    Hello, Kim
    내 성적은 4
    내 성적은 4.500000
    ```
    
  - f-string
    
    ```python
    name = 'Kim'
      score = 4.5
      print(f'Hello, {name}! 성적은 {score}')
      
      pi = 3.141592
      print(f'원주율은 {pi:.3}. 반지름이 2일 때 원의 넓이는 {pi*2*2}')
      
      # output
      Hello, Kim! 내 성적은 4.5
      원주율은 3.14. 반지름이 2일 때 원의 넓이는 12.566368
    ```



#### 3. Nested Quotes (중첩 따옴표)

- 따옴표 안의 따옴표를 표현할 때 사용함
- 작은 따옴표가 들어 있는 경우 큰 따옴표로 문자열을 생성함
- 큰 따옴표가 들어 있는 경우 작은 따옴표로 문자열을 생성함



#### 4. Triple Quotes (삼중 따옴표)

- 작은 따옴표나 큰 따옴표를 삼중으로 사용함
- 따옴표 안에 따옴표를 넣을 때나 여러줄을 나눠 입력할 때 편리함



#### 5. [Indexing/Slicing](https://velog.io/@sunnamgung8/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9D%B8%EB%8D%B1%EC%8B%B1indexing%EC%99%80-%EC%8A%AC%EB%9D%BC%EC%9D%B4%EC%8B%B1slicing)

- 인덱스를 통해 특정 값에 접근할 수 있음




#### 6. Etc Operator

- Concatenation (결합)

  ```python
  'hello, ' + 'python!'
  
  # output
  'hello, python!'
  ```
  
- Repetition (반복)

  ```python
  'hi!' * 3
  
  # output
  'hi!hi!hi!'
  ```
  
- Membership (포함)

  ```python
  'a' in 'apple'
  'app' in 'apple'
  'b' in 'apple'
  
  # output
  True
  True
  False
  ```



### None

- 값이 없음을 표현하기 위해 존재함

- 반환 값이 일반적으로 없는 함수에서 사용하기도 함

  ```python
  a = None
  print(a)
  
  # output
  None
  ```





# Typecasting

#### 1. 자료형 변환

- Python에서 데이터 형태를 서로 변환할 수 있음



#### 2. Implicit Typecasting (암시적 형 변환)

- 사용자가 의도하지 않고, Python 내부적으로 자료형을 변환 하는 경우를 말함

- bool, Numeric Type (int, float, complex)

  ```python
  True + 3
  3 + 5.0
  3 + 4j + 5
    
  # output
  4
  8.0
  (8+4j)
  ```



#### 3. Explicit Typecasting (명시적 형 변환)

- **문자열은 형식에 맞는 것만 가능함**

- str, float → int

  ```python
  '3' + 4
  
  # output
  TypeError: can only concatenate str (not "int") to str
  ```
  
- str, int → float

  ```python
  int('3.5') + 5
  
  # output
  ValueError: incalid literal for int() with base 10: '3.5'
  ```
  
- int, float, list, tuple, dict → str



# Container

### 정의

- 여러 개의 값을 담을 수 있는 것(객체)으로, 서로 다른 자료형을 저장할 수 있음
- 순서가 있는(ordered) 데이터와 순서가 없는(unordered) 데이터로 나뉨
- 순서가 있다는 것이 정렬되어 있다는 뜻은 아님



### Sequence Container

#### 1. 시퀀스형 주요 공통 연산자

| 연산             | 결과                                                    |
| ---------------- | ------------------------------------------------------- |
| s[i]             | s의 i번째 항목, 0에서 시작                              |
| s[i:j]           | s의 i에서 j까지의 슬라이스                              |
| s[i:j:k]         | s의 i에서 j까지 스텝 k의 슬라이스                       |
| s + t            | s와 t의 이어 붙이기                                     |
| s * n 또는 n * s | s를 그 자신에 n번 더하는 것                             |
| x in s           | s의 항목 중 하나가 x와 같으면 True, 그렇지 않으면 False |
| x not in s       | s의 항목 중 하나가 x와 같으면 False, 그렇지 않으면 True |
| len(s)           | s의 길이                                                |
| min(s)           | s의 가장 작은 항목                                      |
| max(s)           | s의 가장 큰 항목                                        |



#### 2. List

1. 정의

- 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음
- 변경 가능(mutable)하며, 반복 가능(iterable)함
- 항상 대괄호 형태로 정의하며, 요소는 콤마로 구분함



2. 생성과 접근

- 대괄호 혹은 list() 를 통해 생성함

  ```python
  my_list = []
  another_list = list()
  ```

- 순서가 있는 시퀀스로 인덱스를 통해 접근이 가능함

  ```python
  a = [1, 2, 3]
  print(a[0])
  
  # output
  1
  ```

- list[i]를 이용해 값에 대한 접근이 가능함



3. 추가와 삭제

- 값 추가는 .append()를 활용해 추가하고자 하는 값을 전달함

  ```python
  even_numbers = [2, 4, 6, 8]
  even_numbers .append(10)
  even_numbers
  
  # output
  [2, 4, 6, 8, 10]
  ```

- 값 삭제는 .pop()을 활용해 삭제하고자 하는 인덱스를 전달함

  ```python
  even_numbers = [2, 4, 6, 8]
  even_numbers .pop(0)
  even_numbers
  
  # output
  [4, 6, 8]
  ```

- 예제

  ```python
  boxes = ['apple', 'banana']
  len(boxes)
  boxes[1]
  boxes[1][0]
  
  # output
  2
  'banana'
  'b'
  ```



#### 3. Tuple

1. 정의

- 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음
- 변경이 불가능(immutable)하나, 반복은 가능(iterable)함
- 항상 소괄호 형태로 정의하며, 요소는 콤마로 구분함



2. 생성과 접근

- 소괄호 혹은 tuple()을 통해 생성함

- 리스트와 동일하게 인덱스로 값에 대해 접근함

  ```python
  a = (1, 2, 3, 1)
  a[1]
  ```

- 값의 변경이 불가능하기 때문에 추가/삭제가 불가능함

  ```python
  a = (1, 2, 3, 1)
  a[1] = '3'
  
  # output
  TypeError Traceback (most recent call last)
  1 a[1] = '3'
  TypeError: 'tuple' object does not support item assignment
  ```



#### 4. Range

1. 정의

- 숫자의 시퀀스를 나타내기 위해 사용함
- 변경이 불가능(immutable)하나, 반복은 가능(iterable)함

   | 연산           | 형태              | 내용                                  |
   | :------------- | :---------------- | :------------------------------------ |
   | range(n)       | 기본형            | 0부터 n-1까지의 시퀀스                |
   | range(n, m)    | 범위 지정         | n부터 m-1까지의 시퀀스                |
   | range(n, m, s) | 범위 및 스텝 지정 | n부터 m-1까지 s만큼 증가시키는 시퀀스 |



### Associative Container

#### 1. Set

1. 정의

- 유일한 값들의 모음 (collection)
- 순서가 없고 중복된 값도 없음
  - 수학에서의 집합과 동일한 구조를 가지며, 집합 연산도 가능함
- 변경 가능(mutable)하며, 반복 가능(iterable)함
  - 단, Set은 순서가 없어 반복의 결과가 정의한 순서와 다를 수 있음



2. 생성

- 중괄호 혹은 set()을 통해 생성함

  ```python
  {1, 2, 3, 1, 2}
  {'hi', 1, 2}
  
  # output
  {1, 2, 3}
  {1, 2, 'hi'}
  ```

- 빈 Set을 만들기 위해서는 반드시 set()을 활용해야 함

- 순서가 없어 별도의 값에 접근할 수 없음

  ```python
  {1, 2, 3}[0]
  
  # output
  TypeError Traceback (most recent call last)
  <ipython-input-95-0c8fa4a2ff15> in <module>
  ----> 1 {1, 2, 3}[0]
  TypeError: 'set' object is not subscriptable
  ```



3. 추가와 삭제

- 값 추가는 .add()를 활용해 추가하고자 하는 값을 전달함

  ```python
  numbers = {1, 2, 3}
  numbers .add(5)
  numbers
  numbers .add(1)
  numbers
  
  # output
  {1, 2, 3, 5}
  {1, 2, 3, 5}
  ```

- 값 삭제는 .remove()를 활용해 삭제하고자 하는 값을 전달함

  ```python
  numbers = {1, 2, 3}
  numbers .remove(1)
  numbers
  numbers .add(5)
  
  # output
  {2, 3}
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  KeyError: 5
  ```



4. 활용

- Set을 활용하면 다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음

- 단, 이후 순서가 무시되므로 순서가 중요한 경우에는 사용할 수 없음

  ```python
  my_list = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']
  len(set(my_list))
  set(my_list)
  
  # output
  4
  {'광주', '대전', '부산', '서울'}
  ```



#### 2. Dictionary

1. 정의

- 키-값(key-value)의 쌍으로 이루어진 모음 (collection)
- key와 value는 :로 구분 되며, 개별 요소는 ,로 구분 됨
- 변경 가능(mutable)하며, 반복 가능(iterable)함
  - 반복하면 키가 반환 됨



2. 생성과 접근

- key와 value가 쌍으로 이뤄진 자료 구조이므로

  - key는 변경이 불가능(immutable)한 데이터만 활용 가능함

    - string, integer, float, boolean, tuple, range

  - value는 모든 값으로 설정이 가능함

    - List, Dictionary 등

    ```python
    dic_c = {[1, 2, 3]: 'hi'}
    
    
    # output
    TypeError Traceback (most recent call last)
    ----> 1 dict_c = {[1, 2, 3]: 'hi'}
    TypeError: unhashable type: 'list'
    ```

  - 접근

    ```python
    movie = {
        'title': '설국열차',
        'genres': ['SF', '액션', '드라마'],
        'open_date': '2013-08-01',
        'time': 126,
        'adult': False,
    }
    
    movie['genres']
    movie['actors']
    
    # output
    ['SF', '액션', '드라마']
    Traceback (most recent call last)
    File "<stdin>", line 1, in <module>
    KeyError: 'actors'
    ```



3. 추가와 변경

- key와 value의 쌍을 추가할 수 있으며, 이미 해당하는 key가 있다면 기존 값이 변경 됨

  ```python
  students = {'홍길동': 100, '김철수': 90}
  students['홍길동'] = 80
  students['박영희'] = 95
  
  # output
  {'홍길동': 80, '김철수': 90}
  {'홍길동': 80, '김철수': 90, '박영희': 95}
  ```




4. 삭제

- .pop()을 활용해 삭제하고자 하는 key를 전달함

  ```python
  students = {'홍길동': 30, '김철수': 25}
  students .pop('홍길동')
  students
  
  # output
  {'김철수': 25}
  ```

- key가 없는 경우에는 KeyError가 발생함

  ```python
  students = {'홍길동': 30, '김철수': 25}
  students .pop('jane')
  
  # output
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  KeyError: 'jane'
  ```

  