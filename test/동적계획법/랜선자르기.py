import sys

sys.stdin = open("input.txt", "r")

n = int(input())
# 각 스텝마다 들어갈 경우의 수
dy = [0] * (n+1)


# f(1)과 f(2)는 1과 2로 이미 고정
dy[1] = 1
dy[2] = 2

for i in range(3, n + 1):
    # 점화식이 f(n) = f(n-1) + f(n-2)
    dy[i] = dy[i-1] + dy[i-2]

print(dy[n])
