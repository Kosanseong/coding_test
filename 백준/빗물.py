import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

h, w = map(int, input().split())
tmp = list(map(int, input().split()))
block = [[0] * w for _ in range(h)]
cnt = 0
b = False
res = []

for idx, i in enumerate(tmp):
    for j in reversed(range(i)):
        block[j][idx] = 1

queue = deque(block)

while queue:
    tmp_arr = queue.popleft()
    for idx, i in enumerate(tmp_arr):
        if i == 1:
            if not res:
                res.append((idx, i))
            else:
                tmp_val = res.pop(0)
                cnt += idx - tmp_val[0] - 1
                res.append((idx, i))

    res = []

print(cnt)



