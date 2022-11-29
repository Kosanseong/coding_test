import sys

sys.stdin = open("input.txt", "r")


def DFS(x):
    if x > 0:
        DFS(x - 1)
        print(x)  # 재귀는 스택을 활용함


# 재귀 함수와 스택
if __name__ == "__main__":
    n = int(input())
    DFS(n)
