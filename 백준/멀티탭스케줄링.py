import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))
queue = deque(a)
current = []
cnt = 0

while len(current) != n:
    tmp = queue.popleft()
    if tmp not in current:
        current.append(tmp)


while queue:
    obj = queue.popleft()
    if obj not in queue:



# 123451
