import sys

sys.stdin = open("input.txt", "r")


def DFS(L, sum, time):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L + 1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)

if __name__ == "__main__":
    n, m = map(int, input().split())
    pv = []
    pt = []
    for i in range(5):
        q, t = map(int, input().split())
        pv.append(q)
        pt.append(t)
    res = -2147000000
    DFS(0, 0, 0)
    print(res)


