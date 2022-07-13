# 10을 넣었을 때 55가 나오게 하라
# while문
i = int(input())
n = 0
sum = 0
while n < i:
    n += 1
    sum += n
print(sum)

# for문
n = 0
for i in range(1, int(input())+1):
    n += i
print(n)