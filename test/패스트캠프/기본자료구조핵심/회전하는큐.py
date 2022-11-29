import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

a = list(map(int, input().split()))
arr = [i+1 for i in range(n)]
cnt = 0
queue = deque(arr)

for i in a:
    index = queue.index(i)
    if index <= len(queue)//2:
        while True:
            if i == queue[0]:
                queue.popleft()
                break
            else:
                tmp = queue.popleft()
                queue.append(tmp)
                cnt += 1
    else:
        while True:
            if i == queue[0]:
                queue.popleft()
                break
            else:
                tmp = queue.pop()
                queue.insert(0, tmp)
                cnt += 1

print(cnt)
