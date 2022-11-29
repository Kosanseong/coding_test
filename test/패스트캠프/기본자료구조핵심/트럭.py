import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

n, w, L = map(int, input().split())

a = list(map(int, input().split()))
tmp = deque([0] * w)
d = deque(a)
time = 0
weight = 0
while True:
    if not d and sum(tmp) == 0:
        break
    if d and sum(tmp) + d[0] <= L:
        x = d.popleft()
        tmp.popleft()
        tmp.append(x)
        time += 1
    else:
        x = tmp.popleft()
        if d and sum(tmp) + d[0] <= L:
            tmp.append(d.popleft())
        else:
            tmp.append(0)
        time += 1

print(time)


