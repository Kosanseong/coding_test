import sys

sys.stdin = open("input.txt", "r")

def DFS(L, num):
    global cnt
    if L == m:
        for x in res:
            print(x, end=' ')
        cnt += 1
        print()
    else:
        for i in range(num, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1, i + 1)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    ch = [0] * (n+1)
    cnt = 0
    res = [0]*m
    DFS(0, 1)
    print(cnt)

