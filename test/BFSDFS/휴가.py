import sys

sys.stdin = open("input.txt", "r")

def DFS(L, sum):
    global res
    if L == n + 1:
        if sum > res:
            res = sum
    else:
        if L + pt[L] <= n + 1:
            DFS(L+pt[L], sum + pv[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    n = int(input())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(b)
        pt.append(a)
    pv.insert(0, 0)
    pt.insert(0, 0)
    res = -2147000000
    DFS(1, 0)
    print(res)
