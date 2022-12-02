import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
board = []
# 거리를 나타낸 2차원 배열 board가 1인 곳에 도착하면 해당 지점에 거리를 입력
dis = [[0] * m for _ in range(n)]
queue = deque()

for _ in range(n):
    board.append(list(map(int, input())))

# 시작 지점
queue.append((0, 0))
board[0][0] = 0
dis[0][0] = 1

while queue:
    tmp = queue.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x < n and 0 <= y < m and board[x][y] == 1:
            '''
            board를 0으로 만드는 것은 최단 거리이기 때문에 
            다른 지점을 갔다 돌아오는 길은 무조건 최단거리보다 길기 때문이다.
            그렇기 때문에 갔다 돌아오는 길은 해당 사항이 없기 때문에 고려할 필요가 없다
            '''
            board[x][y] = 0
            '''
            거리를 +1하는 이유는 x,y 지점은 tmp[0], tmp[1] 지점에
            다음 지점이기 때문에 거리로 보면 전 지점보다 1 더 증가된 상태이다.
            '''
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            queue.append((x, y))

# 거리를 쟀기 때문에 도착지점의 수를 출력하면 된다.
print(dis[n-1][m-1])
