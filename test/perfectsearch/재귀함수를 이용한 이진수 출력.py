import sys

sys.stdin = open("input.txt", "r")

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2) #복귀 지점
        print(x%2, end=' ')


# 재귀 함수와 스택
if __name__ == "__main__":
    n = int(input())
    DFS(n)
