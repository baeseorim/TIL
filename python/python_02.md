# Control Statement (제어문)

- Python은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행함
- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속해서 실행(반복)할 수 있는 제어가 필요함
- 순서도(Flow Chart)로 표현이 가능함

ㅤ

ㅤ

## Conditional Statement

#### 1. Conditional Statement (조건문)

- 참/거짓을 판단할 수 있는 조건식과 함께 사용 됨

ㅤ

#### 2. 기본 형식

- expression에는 참/거짓에 대한 조건식이 들어감

- 조건이 참인 경우 이후 들여쓰기 되어 있는 코드 블럭을 실행함

- 이외의 경우 else 이후 들여쓰기 되어 있는 코드 블럭을 실행함

- else는 선택적으로 활용이 가능함

  ```python
  if <expression>:
      # Run this code block
  else:
      # Run this code block
  ```

- 예제

  ```python
  # 조건문을 통해 변수 num의 값의 홀수/짝수 여부를 출력하시오.
  # 이때 num은 input을 통해 사용자로부터 입력 받으시오.
  
  num = int(input())
  if num % 2 == :
      print('홀')
  else:
      print('짝')
  ```

ㅤ

#### 3. 복수 조건문

- 복수의 조건식을 활용할 경우 elif를 활용하여 표현함

  ```python
  if <expression>:
      # Code block
  elif <expression>:
      # Code block
  elif <expression>:
      # Code block
  else:
      # Code block
  ```

- 조건식을 동시에 검사하지 않고 순차적으로 비교함

- 예제

  ```python
  # 다음은 미세먼지 농도에 따른 등급일 때,
  # dust 값에 따라 등급을 출력하는 조건식을 작성하시오.
  
  dust = 80
  if dust > 150:
      print('매우 나쁨')
  elif dust > 80:
      print('나쁨')
  elif dust > 30:
      print('보통')
  else:
      print('좋음')
  print('미세먼지 확인 완료')
  ```

ㅤ

#### 4. 중첩 조건문

- 다른 조건문에 중첩되어 사용될 수 있음

- 들여쓰기에 유의하여 작성해야함

  ```python
  if <expression>:
      # Code block
      if <expression>:
          # Code block
  else:
      # Code block
  ```

- 예제

  ```python
  # 아래의 코드에서 중첩 조건문을 활용하여 미세먼지 농도(dust 값)이 300이 넘는 경우 '실외 활동을 자제하세요'를 추가적으로 출력하고 음수인 경우 '값이 잘못 되었습니다'를 출력하시오.
  dust = 80
  if dust > 150:
      print('매우 나쁨')
  elif dust > 80:
      print('나쁨')
  elif dust > 30:
      print('보통')
  else:
      print('좋음')
  print('미세먼지 확인 완료')
  
  dust = 10
  if dust > 150:
      print('매우 나쁨')
      if dust > 300:
          print('실외 활동을 자제하세요.')
  elif dust > 80:
      print('나쁨')
  elif dust > 30:
      print('보통')
  else:
      if dust >= 0:
          print('좋음')
      else:
          print('값이 잘못되었습니다.')
  ```
  

ㅤ

#### 5. Conditional Expression (조건 표현식)

- 일반적으로 조건에 따라 값을 할당할 때 활용 됨

  ```python
  <true인 경우의 값> if <expression> else <false인 경우의 값>
  ```

- 예제

  ```python
  # num이 정수일 때, 아래의 코드는 무엇을 위한 코드일까요?
  value = num if num >= 0 else -num
  
  # 절대값을 저장하기 위한 코드
  ```

  ```python
  # 아래의 코드는 무엇을 위한 코드일까요?
  num = int(input())
  value = num if num >= 0 else -num
  print(value)
  
  # 절대값 계산기
  ```

  ```python
  # 다음의 코드와 동일한 조건 표현식을 작성하시오.
  num = 2
  if num % 2:
      result = '홀'
  else:
      result = '짝'
  print(result)
  
  num = 2
  result = '홀' if num % 2 else '짝'
  print(result)
  ```

  ```python
  # 다음의 코드와 동일한 조건문을 작성하시오.
  num = -5
  value = num if num >= 0 else 0
  print(value)
  
  num = -5
  if num >= 0:
      value = num
  else:
      value = 0
  print(value)
  ```

ㅤ

## Loop Statement

#### 1. Loop Statement (반복문)

- 특정 조건에 도달할 때까지 계속 반복되는 일련의 문장을 말함

ㅤ

#### 2. while문

- 조건식이 **참인 경우** 들여쓰기가 되어 있는 코드 블록이 실행 됨

- 코드 블록이 모두 실행된 후, 다시 조건식을 검사하면서 반복적으로 실행 됨

- 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야 함

- 무한 루프를 하지 않기 위해선 종료 조건이 반드시 필요함

- 예제

  ```python
  # 1부터 사용자가 입력한 양의 정수까지의 총합을 구하는 코드를 작성하시오.
  
  # 값 초기화
  n = 0
  total = 0
  user_input = int(input())
  
  while n <= user_input:
      total += n
      n += 1
  print(total)
  
  while n < user_input:
      n += 1
      total += n
  print(total)
  ```

ㅤ

#### 3. for문

- 시퀀스(string, tuple, list, range)를 포함한 순회 가능(iterable)한 객체 요소를 모두 순회함

- 처음부터 끝까지 모두 순회하면 종료되므로 별도의 종료 조건이 필요하지 않음

- 일반 형식 (iterable)
  - 순회할 수 있는 자료형(str, list, dict 등)
  - 순회형 함수(range, enumerate)

- String 순회

  ```python
  # 사용자가 입력한 문자를 한 글자씩 세로로 출력하시오.
  chars = input()
  
  for char in chars:
      print(char)
  ```

  ```python
  # 사용자가 입력한 문자를 range를 활용하여 한 글자씩 출력하시오.
  chars = input()
  
  for idx in range(len(chars)): # index를 기준으로 순회함
      print(chars[idx])
  ```

- Enumerate 순회

  - 인덱스와 객체를 쌍으로 담아 열거형으로 객체를 반환함

  - (index, value) 형태의 tuple로 구성된 열거 객체를 반환함

  - 예시

    ```python
    enumerate(members) # <enumerate at 0x105d3e100>
    list(enumerate(members)) # [(0, '민수'), (1, '영희'), (2, '철수')]
    list(enumerate(members, start=1)) # [(1, '민수'), (2, '영희'), (3, '철수')]
    ```

- Dictionary 순회

  - 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용함

  - 예시

    ```python
    grades = {'john': 80, 'eric': 90}
    for name in grades:
        print(name, grades[name])
    
    # output
    john 80
    eric 90
    ```

ㅤ

#### 4. 반복문 제어

1. break

   - 반복문을 종료 시킴

   - 예시

     ```python
     n = 0
     while True:
         if n == 3:
             break
         print(n)
         n += 1
     
     # output
     0
     1
     2
     ```

     ```python
     for i in range(10):
         if i > 1:
             print('0과 1만 필요해!')
             break
         print(i)
     
     # output
     0
     1
     0과 1만 필요해!
     ```

2. continue

   - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행함

   - 예시

     ```python
     for i in range(6):
         if i % 2 == 0:
             continue
         print(i)
     
     # output
     1
     3
     5
     ```

3. for-else

   - 반복문을 끝까지 실행한 이후에 else문을 실행함

   - break문을 통해 중간에 종료되는 경우 else문은 실행되지 않음

   - 예시

     ```python
     for char in 'apple':
         if char == 'b':
             print('b!')
             break
     else:
         print('b가 없습니다.')
         
     # output
     b가 없습니다.
     ```

     ```python
     for char in 'banana':
         if char == 'b':
             print('b!')
             break
     else:
         print('b가 없습니다.')
     
     # output
     b!
     ```



