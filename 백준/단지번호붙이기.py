import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0
visited = [[False] * n for _ in range(n)]
result = []
for _ in range(n):
    s = list(map(int, input()))
    a.append(s)

def DFS(x,y):
    global cnt
    visited[x][y] = True
    if a[x][y] == 1:
        cnt += 1

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and a[xx][yy] == 1 and visited[xx][yy] == False:
            DFS(xx, yy)

for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and visited[i][j] == False:
            DFS(i, j)
            result.append(cnt)
            cnt = 0


result = sorted(result)

print(len(result))
for i in result:
    print(i)
