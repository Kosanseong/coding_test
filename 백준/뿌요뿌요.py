import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10000)
a = []
for _ in range(12):
    a.append(list(input()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0
last_cnt = -1
cnt_block = 0
tmp = []

def arrange(y):
    tmp_cnt = 0
    for i in reversed(range(12)):
        if a[i][y] == '.':
            tmp_cnt += 1
        else:
            a[i + tmp_cnt][y] = a[i][y]
            a[i][y] = '.'

def DFS(x, y, color):
    global cnt_block
    a[x][y] = '.'
    cnt_block += 1
    tmp.append((x, y))
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < 12 and 0 <= yy < 6 and a[xx][yy] == color:
            DFS(xx, yy, color)


while True:
    cnt_block = 0
    if cnt == last_cnt:
        break
    for i in reversed(range(12)):
        for j in reversed(range(6)):
            if a[i][j] != '.':
                color = a[i][j]
                DFS(i, j, color)
                if cnt_block >= 4:
                    cnt += 1
                    last_cnt = cnt
                    tmp = sorted(tmp, key=lambda x: x[1])
                    while tmp:
                        y = tmp.pop()[1]
                        arrange(y)
                    break
                else:
                    for k in tmp:
                        a[k[0]][k[1]] = color
                tmp = []


print(cnt)
