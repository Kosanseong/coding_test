import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

case = int(input())

for i in range(case):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    tmp = []
    cnt = 0
    for j in range(n):
        tmp.append((arr[j], j))

    queue = deque(tmp)

    while queue:
        maxq = max(queue)
        left = queue.popleft()

        if maxq[0] != left[0]:
            queue.append(left)
        else:
            cnt += 1
            if left[1] == m:
                print(cnt)
                break




