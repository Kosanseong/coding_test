import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
tmp = []
for i in range(n):
    tmp.append((i+1, a[i]))
d = deque(tmp)
result = []
i = d.popleft()
result.append(i[0])

while d:
    if len(d) == 1:
        result.append(d.popleft()[0])
        break
    if i[1] > 0:
        for _ in range(i[1] - 1):
            d.append(d.popleft())
        i = d.popleft()
        result.append(i[0])
    else:
        x = i[1] * -1
        for _ in range(x):
            d.appendleft(d.pop())
        i = d.popleft()
        result.append(i[0])

for i in result:
    print(i, end=' ')
