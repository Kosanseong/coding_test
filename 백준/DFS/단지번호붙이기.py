import sys
sys.stdin = open("input.txt", "r")

n = int(input())
location = [[]*n for i in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
cnt = 0
tmp = []

for i in range(n):
    location[i] = list(map(int, input()))

def DFS(x, y):
    global cnt
    location[x][y] = 0

    if x == n-1 and y == n-1:
        return
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if n > xx >= 0 and n > yy >= 0 and location[xx][yy] == 1:
                location[xx][yy] = 0
                cnt += 1
                DFS(xx, yy)

DFS(0, 0)
print(tmp)
