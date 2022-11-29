import sys
sys.stdin = open("input.txt", "rt")

n, m, v = map(int, input().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    l1, l2 = map(int, input().split())
    arr[l1][l2] = 1
    arr[l2][l1] = 1


ch = [0]*(n+1)
result = []
def DFS(v):
    if sum(ch) == n:
        return
    else:
        if ch[v] == 0:
            result.append(v)
            ch[v] = 1
            print(ch)

        for i in range(len(arr[v])):
                if arr[v][i] == 1:
                    arr[v][i] = 0
                    arr[i][v] = 0
                    DFS(i)
DFS(v)
print(result)
