import sys

sys.stdin = open("input.txt", "r")


def DFS(L, sum):
    global cnt
    if sum > T:
        return
    if L == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(n[L] + 1): # +1을 해줘야 끝까지 돌지 바보야
            DFS(L+1, sum + (i*p[L]))

if __name__ == "__main__":
    T = int(input())
    k = int(input())
    p = list()
    n = list()
    cnt = 0
    for i in range(k):
        p1, n1 = map(int, input().split())
        p.append(p1)
        n.append(n1)
    DFS(0, 0)
    print(cnt)
