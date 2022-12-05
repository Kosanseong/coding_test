import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n, m, k = map(int, input().split())

path = [[0] * m for _ in range(n)]
queue = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 1
maximum = -1

for _ in range(k):
    n1, n2 = map(int, input().split())
    path[n1 - 1][n2 - 1] = 1

for i in range(n):
    for j in range(m):
        if path[i][j] == 1:
            queue.append((i, j))
            path[i][j] = 0
            while queue:
                tmp = queue.popleft()
                for l in range(4):
                    x = tmp[0] + dx[l]
                    y = tmp[1] + dy[l]
                    if 0 <= x < n and 0 <= y < m and path[x][y] == 1:
                        cnt += 1
                        queue.append((x, y))
                        path[x][y] = 0

            maximum = max(maximum, cnt)
            cnt = 1

print(maximum)
