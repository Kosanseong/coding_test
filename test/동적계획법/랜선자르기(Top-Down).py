import sys

sys.stdin = open("input.txt", "r")

n = int(input())
# 각 스텝마다 들어갈 경우의 수(메모이제이션)
dy = [0] * (n+1)
dy[1] = 1
dy[2] = 2

def DFS(n):
    # dy 배열에 값이 있다면 굳이 연산할 필요없이 리턴해버린다
    if dy[n] != 0:
        return dy[n]

    return DFS(n-1) + DFS(n-2)

print(DFS(n))
