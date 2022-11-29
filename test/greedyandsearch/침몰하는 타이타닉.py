import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr = deque(arr)
count = 0

while arr:
    if len(arr) == 1:
        count += 1
        break

    if arr[0] + arr[-1] > m:
        arr.pop()
        count += 1
    else:
        arr.popleft() # 그냥 pop시킬 경우 앞자리가 빠지면서 앞으로 값들이 이동하는 연산이 발생하여 비효율 그렇기 때문에 deque를 사용해야함
        arr.pop()
        count += 1

print(count)
