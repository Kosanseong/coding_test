import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

h, w = map(int, input().split())
tmp = list(map(int, input().split()))
block = [[0] * w for _ in range(h)]
cnt = 0
res = []

'''
입력을 2차원 배열로 역방향으로 넣어준다. 바닥이 위로오게
'''
for idx, i in enumerate(tmp):
    for j in reversed(range(i)):
        block[j][idx] = 1

queue = deque(block)

while queue:
    # 각줄을 뽑아 낸다.
    tmp_arr = queue.popleft()
    for idx, i in enumerate(tmp_arr):
        if i == 1:
            # res배열에 아무것도 없을 땐 해당 위치를 넣어준다
            if not res:
                res.append(idx)
            else:
                # 전 값이 있을 경우 idx만 비교하여 cnt에 값을 넣어준다.
                tmp_val = res.pop(0)
                cnt += idx - tmp_val - 1
                res.append(idx)

    res = []

print(cnt)



