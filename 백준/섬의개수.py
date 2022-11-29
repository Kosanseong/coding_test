import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]
cnt = 0
result = []

def DFS(x, y):
    island[x][y] = 0
    for i in range(8):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < h and 0 <= yy < w and island[xx][yy] == 1:
            DFS(xx, yy)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island = []
    for _ in range(h):
        island.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                DFS(i, j)
                cnt += 1

    result.append(cnt)
    cnt = 0

for i in result:
    print(i)
