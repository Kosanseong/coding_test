import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

m, n = map(int, input().split())
box = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
days = 0
queue = deque()

for _ in range(n):
    tmp = list(map(int, input().split()))
    box.append(tmp)

for i in range(n):
    for j in range(m):
        '''
        이부분에서 조금 헤맸는데 처음에 만들었을 때 1을 발견한 시점부터 bfs를 돌았다
        하지만 문제는 양쪽에 토마토가 있다면 동시에 익어가야 한다는 것이었는데
        그냥 돌아버리니 처음 발견한 곳부터 계속 익힌걸로해서 원래 나와야 할 답보다 더 크게 나왔다.
        '''
        if box[i][j] == 1:
            queue.append((i, j))


# 보통 큐를 돌려 bfs를 하는 식
while queue:
    tmp = queue.popleft()
    for k in range(4):
        x = tmp[0] + dx[k]
        y = tmp[1] + dy[k]
        if 0 <= x < n and 0 <= y < m and box[x][y] == 0:
            queue.append((x, y))
            '''
            다음에 익는 토마토는 전날 익은 토마토보다 1일 더 늦기 때문에 전날에 +1 해준다.
            '''
            box[x][y] = box[tmp[0]][tmp[1]] + 1

'''
0이 하나라도 있으면 안 익은 것이 있다는 것이기 때문에
-1 출력
'''
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    # 최댓값을 찾아줘야한다.
    days = max(days, max(i))

'''
box배열 내에서 최대값을 찾은 것이기 때문에 원래 값보다 1이 더높다
따라서 시작인 1을 빼야한다.
'''
print(days - 1)
