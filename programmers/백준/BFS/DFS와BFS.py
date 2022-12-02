import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n, m, v = map(int, input().split())

ch = [0] * (n+1) # 이미 방문한 곳 이라면 1로
graph = [[0] * (n+1) for _ in range(n+1)] # 양방향 간선이기 때문에 2차원 배열에 마킹
# ch를 사용하지 않아도 됨

for _ in range(m):
    # 간선의 노드들을 graph에 마킹
    n1, n2 = map(int, input().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1

# 실제론 입력값이 적어 굳이 큐를 만들지 않아도 되지만 BFS는 큐를 사용하기에
v_arr = [v]
# 초기 노드를 이미 방문한 것으로
ch[v] = 1
queue = deque(v_arr)


while queue:
    tmp = queue.popleft()
    print(tmp, end=' ')
    for i in range(1, n + 1):
        # 방문하지 않고 tmp와 연결된 노드라면
        if ch[i] == 0 and graph[tmp][i] == 1:
            # 방문 표시를 하고
            ch[i] = 1
            # 큐에 집어 넣음
            queue.append(i)


