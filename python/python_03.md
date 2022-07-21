# Function

#### 1. 정의

- 특정한 기능을 하는 코드의 조각(묶음)
- 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요시에만 호출하여 간편히 사용할 수 있음

ㅤ

#### 2. 사용자 함수 (Custom Function)

- 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성할 수 있음

  ```python
  def function_name:
      # Code block
      return returning_value
  ```

ㅤ

#### 3. 함수를 사용하는 이유

- 코드 중복을 방지할 수 있고 재사용이 용이하기 때문

  ```python
  # function
  values = [100, 75, 85, 90, 65, 95]
  total = 0
  cnt = 0
  
  for value in values:
      total += value
      cnt += 1
  mean = total / cnt
  
  total_var = 0
  for value in values:
      total_var += (value - mean) ** 2
      
  sum_var = total_var / cnt
  target = sum_var
  
  while True:
      root = 0.5 * (target + (sum_var/target))
      if (abs(root - target) < 0.00000000001):
          break
      target = root
  std_dev = target
  print(std_dev)
  
  # 내장 함수(Built-in Function)를 활용
  import math
  values = [100, 75, 85, 90, 65, 95]
  mean = sum(values) / len(values)
  sum_var = sum(pow(value - mean, 2) for value in values) / len(values)
  std_dev = math.sqrt(sum_var)
  print(std_dev)
  
  # pstdev 함수(Python 표준 라이브러리 statistics)를 활용
  import statistics
  values = [100, 75, 85, 90, 65, 95]
  statistics.pstdev(values)
  ```


ㅤ

ㅤ

# 함수 기본 구조

### Define & Call (선언과 호출)

- 함수의 선언은 def 키워드를 활용함

- 들여쓰기를 통해 실행될 코드 블록(Function Body)을 작성함
  
- function body 앞에 docstring 작성을 선택적으로 할 수 있으며, 작성 시에는 반드시 첫번째 문장에 문자열 """을 배치함

- 함수는 parameter를 넘겨줄 수 있음

- **함수는 호출 되면 코드를 실행하고 return 값을 반환하며 종료 됨**
  
- 함수는 함수명()으로 호출하며, parameter가 있는 경우 함수명(값1, 값2, ⋯)으로 호출함
  
- 예시

  ```python
  num1 = 0
  num2 = 1
  
  def func1(a, b):
      return a + b
  
  def func2(a, b):
      return a - b
  
  def func3(a, b):
      return func1(a, 5) + func2(5, b)
  
  result = func3(num1, num2)
  print(result)
  
  # output
  9
  ```

ㅤ

### Input (입력)

#### 1. [매개변수(Parameter)와 인자(Argument)](https://7942yongdae.tistory.com/155)

- parameter : 함수를 실행할 때 함수 내부에서 사용되는 식별자

- argument : 함수를 호출할 때 넣어주는 값

  ```python
  def function(ham): # parameter : ham
      return ham
  function('spam') # argument : 'spam'
  ```

ㅤ

#### 2. 인자

- 함수 호출 시 함수의 parameter를 통해 전달되는 값을 말함

- 소괄호 안에 할당 됨
  - 필수 argument : 반드시 전달되어야 하는 argument
  - 선택 argument : 값을 전달하지 않아도 되는 경우에는 기본 값이 전달 됨

ㅤ

#### 3. 위치 인자 (Positional Arguments)

- 기본적으로 함수 호출 시 argument는 위치에 따라 함수 내에 전달 됨

  ```python
  def add(x, y):      add(2, 3) # 2는 x로 3은 y로
      return x + y
  ```

ㅤ

#### 4. 키워드 인자 (Keyword Arguments)

- 변수의 이름으로 직접 특정 argument를 전달할 수 있음

- keyword argument 다음에 positional argument를 활용할 수는 없음

  ```python
  def add(x, y):      add(x=2, y=5)
      return X + y    add(2, y=5)
  ```

ㅤ

#### 5. 기본값 (Default Arguments Values)

- 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함

- 정의된 것보다 더 적은 개수의 argument들로 호출될 수 있음

  ```python
  def add(x, y=0):      add(2) # y는 0이어도 되고 아니어도 되고
      return x + y
  ```

ㅤ

#### 6. 정해지지 않은 개수의 arguments

- 여러 개의 positional argument를 하나의 필수 parameter로 받아서 사용함
- 몇개의 positional argument를 받을지 모르는 함수를 정의할 때 유용함

- argument들은 튜플로 묶여 처리되며, parameter에 *를 붙여 표현함

  ```python
  def add(*args):         add(2)
      for arg in args:    add(2, 3, 4, 5)
      print(arg)
  ```

ㅤ

#### 7. 정해지지 않은 개수의 keyword arguments

- 함수가 임의의 개수 argument를 keyword argument로 호출될 수 있도록 지정함

- argument들은 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현함

  ```python
  def family(**kwargs):
      for key, value in kwargs:
          pring(key, ":", value)
  family(father='John', mother='Jane', me='John Jr.')
  ```

ㅤ

### Scope (범위)

#### 1. 정의와 종류

- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분 됨

- scope
  - global scope : 코드 어디에서든 참조할 수 있음
  - local scope : 함수가 만든 scope로 함수 내부에서만 참조가 가능함

- variable
  - global variable : global scope에 정의된 변수
  - local variable : local scope에 정의된 변수

ㅤ

#### 2. 객체 수명주기 (Object Lifecycle)

- 객체는 각자의 수명주기가 존재함
  - built-in scope : 파이썬이 실행된 이후부터 영원히 유지 됨
  - global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지 됨
  - local scope : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지 됨

- 예시

  ```python
  def func():
      a = 20
      print('local', a)
      
  func()
  print('global', a)
  
  #output
  local 20
  3 print('local', a)
  5 func()---->
  6 print('global', a)
  NameError: name 'a' is not defined
  # a는 local scope에서만 존재함
  ```

ㅤ

#### 3. 이름 검색 규칙 (Name Resolution)

- 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace) 에 저장되어 있음

- 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름
  - local scope : 함수

  - enclosed scope : 특정 함수 상위의 함수

  - global scope : 함수 밖의 변수, import 모듈
  - built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성

- 즉, 함수 내에서는 바깥 scope의 변수에 접근이 가능하나 수정은 할 수 없음

- 예시

  ```python
  print(sum)
  print(sum(range(2)))
  sum = 5
  print(sum)
  print(sum(range(2)))
  
  # output
  <built-in function sum>
  1
  5
  TypeError Traceback (most recent call last)
  3 sum = 5
  4 print(sum)---->
  5 print(sum(range(2)))
  TypeError:'int' object is not callable
  ```

ㅤ

### Output (결과값)

- 반드시 하나의 값만 return 함

- 명시적인 return이 없는 경우에도 None을 반환함

- return과 동시에 실행이 종료 됨

- return문을 한번만 사용하면서 두 개 이상의 값을 반환하기 위해서 tuple 반환을 이용함

  ```python
  def minus_and_product(x, y):
      return x- y
      return x * y
  minus_and_product(4, 5)
  
  # output
  -1
  ```

  ```python
  def minus_and_product(x, y):
      return x - y, x * y
  minus_and_product(4, 5)
  
  # output
  (-1, 20)
  ```

- return과 print의 차이점
  - return : 함수 안에서 값을 반환하기 위해 사용되는 키워드
  - print : 출력을 위해 사용되는 함수

ㅤ

ㅤ

# 함수 응용

- 파이썬 인터프리터에는 사용할 수 있는 수많은 함수와 type이 내장되어 있음

- map(function, iterable)
  - 순회 가능한 데이터구조(iterable)의 모든 요소에 function을 적용하고, 그 결과를 map object로 반환함
  
    ```python
    numbers = [1, 2, 3]
    result = map(str, numbers)
    print(result, type(result))
    list(result)
    
    # output
    <map object at 0x10e2ca100><class 'map'>
    ['1', '2', '3']
    ```
  
  - 알고리즘 문제 풀이 시 input 값들을 숫자로 바로 활용하고 싶을 때 용이함
  
    ```python
    n, m = map(int, input().split())
    print(n, m)
    print(type(n), type(m))
    
    # output
    3 5
    <class 'int'><class'int'>
    ```

