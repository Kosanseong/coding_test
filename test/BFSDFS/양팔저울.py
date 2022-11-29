import sys

sys.stdin = open("input.txt", "r")
# 왼쪽에 둘거나 오른쪽에 둘거냐 안놓을거냐

def DFS(L, sum):
    global res
    if L == k:
        if S >= sum > 0:
            res.add(sum)
    else:
        DFS(L+1, sum+p[L])
        DFS(L+1, sum-p[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    k = int(input())
    p = list(map(int, input().split()))
    S = sum(p)
    res = set()
    DFS(0, 0)
    print(S - len(res))

