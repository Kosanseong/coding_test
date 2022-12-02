import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
# W 혹은 B를 발견 했을 때 상하 좌우를 나아가기 위한 좌표 배열(대각선 포함X)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

graph = [] # 인풋으로 들어오는 아군 적군의 값을 담기위한 배열

power = [0, 0] # W의 파워 0번째, B의 파워 1번째

queue = deque() # 아군의 좌표를 담기위한 큐

p = '' # 기준이 되는 아군의 색상

for _ in range(m):
    graph.append(list(input()))

for i in range(m):
    for j in range(n):
        cnt = 0 # 몇명의 아군이 발견되었는지 확인하기 위한 카운트
        if graph[i][j] != 'D': # D는 이미 확인하고 지나간 자리일 경우 Done을 표현
            queue.append((i, j)) # D가 아닌 즉 W 혹은 B의 자리를 큐에 담는다
            p = graph[i][j] # 최초 발견한 아군의 색상을 저장한다
            graph[i][j] = 'D' # 이미 확인하고 지나간 자리인 것을 표시
            cnt += 1 # 아군수를 1증가
            while queue:
                tmp = queue.popleft() # 큐에 담긴 발견한 좌표를 꺼내어 저장

                for k in range(4): # 상하좌우 4번을 돌기 때문에 4번을 돌면 된다.
                    # 상하 좌우의 좌표를 만들기 위한 식
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < m and 0 <= y < n and graph[x][y] == p: # x와 y가 주어진 m과 n 사이일 경우와 graph[x][y]가 최초 발견한 색상과 동일할 경우
                        cnt += 1
                        queue.append((x, y)) # 발견한 좌표이기 때문에 큐에 담는다
                        graph[x][y] = 'D'

            # BFS 한 사이클이 끝나면 최초 발견 아군의 색상에 따라 power 배열에 cnt의 제곱을 더한다.
            if p == 'W':
                power[0] += cnt * cnt
            else:
                power[1] += cnt * cnt

for i in power:
    print(i, end=' ')
