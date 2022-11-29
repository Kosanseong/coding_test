import sys

sys.stdin = open("input.txt", "r")

def DFS(L):
    global cnt
    if L == n:
        cnt += 1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for j in range(1, n + 1):
            if a[L][j] == 1 and ch[j] == 0:
                ch[j] = 1
                path.append(j)
                DFS(j) # L에서 i로 넘어갔기 때문에 i를 넘겨준다.
                path.pop()
                ch[j] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(m):
        n1, n2 = map(int, input().split())
        a[n1][n2] = 1

    cnt = 0
    ch = [0]*(n+1)
    ch[1] = 1
    path = []
    path.append(1)
    DFS(1)
    print(cnt)
