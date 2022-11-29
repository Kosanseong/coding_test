import sys
from collections import deque
sys.stdin = open("input.txt", "r")

# BFS 는 레벨 탐색이고 BFS는 queue를 사용 한다
# 최단 거리로 갈 때 보통 사용 한다.
MAX = 10000
n, m = map(int, input().split())
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)

while dQ:
    now = dQ.popleft()
    if now == m:
        break
    for next in(now-1, now+1, now+5): # 이러면 3방향을 한번씩 포문을 돌릴 수 있다
        if MAX >= now > 0:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1

print(dis[m])



