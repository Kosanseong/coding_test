import sys

sys.stdin = open("input.txt", "r")

n = int(input())
# 각 스텝마다 들어갈 경우의 수
dy = [0] * (n+1)

def DFS(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return DFS(n-1) + DFS(n-2)

print(DFS(n))
