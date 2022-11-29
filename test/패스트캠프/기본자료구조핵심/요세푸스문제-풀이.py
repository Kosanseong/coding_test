import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
n, k = map(int, input().split())

a = [i+1 for i in range(n)]
queue = deque(a)
i = 1
tmp = []
for i in range(n):
    for _ in range(k-1):
        x = queue.popleft()
        queue.append(x)
    x = queue.popleft()
    tmp.append(x)

print('<', end='')
for i in range(len(tmp)):
    if i < len(tmp) - 1:
        print(tmp[i], end=', ')
    else:
        print(tmp[i], end='')
print('>')
