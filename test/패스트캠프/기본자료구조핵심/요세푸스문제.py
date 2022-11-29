import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())

a = [i+1 for i in range(n)]
queue = deque(a)
i = 1
tmp = []
while queue:
    if i == k:
        tmp.append(queue.popleft())
        i = 1
    elif len(queue) == 1:
        tmp.append(queue.popleft())
    else:
        queue.append(queue.popleft())
        i += 1

print('<', end='')
for i in range(len(tmp)):
    if i < len(tmp) - 1:
        print(tmp[i], end=', ')
    else:
        print(tmp[i], end='')
print('>')
