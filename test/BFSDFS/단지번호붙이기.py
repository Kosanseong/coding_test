import sys

sys.stdin = open("input.txt", "r")

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt
    board[x][y] = 0
    cnt += 1
    if x == n-1 and y == n-1:
        return
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
                DFS(xx, yy)


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt = 0
                DFS(i, j)
                res.append(cnt)

    print(len(res))
    res.sort()
    for x in res:
        print(x)
