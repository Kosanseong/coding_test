import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)

case = int(input())
cnt = 0
result = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y):
    location[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < m and location[xx][yy] == 1:
            DFS(xx, yy)

for _ in range(case):
    m, n, k = map(int, input().split()) # m = 배추밭 가로길이 n = 세로길이 k = 배추 심어진 갯수
    location = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        location[x][y] = 1

    for i in range(n):
        for j in range(m):
            if location[i][j] == 1:
                DFS(i, j)
                cnt += 1

    result.append(cnt)
    cnt = 0

for i in result:
    print(i)
