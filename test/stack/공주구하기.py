import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())
que = list(range(1, n+1))
que = deque(que)

cnt = 1

while len(que) > 1:
    if cnt == k:
        que.popleft()
        cnt = 1
    else:
        que.append(que.popleft())
        cnt += 1

print(que[0])


'''
while que:
    for _ in range(k-1):
        cur = que.popleft()
        que.append(cur)
    que.popleft()
    if len(dq)==1:
        print(que[0])
        que.popleft()
'''
