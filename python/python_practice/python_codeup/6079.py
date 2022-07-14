n = int(input())
sum = 0
for i in range(1, n+1):
    sum = sum + i
    if sum >= n:
        print(i)

# 자꾸 i에서 n까지 출력 돼 흑흑......