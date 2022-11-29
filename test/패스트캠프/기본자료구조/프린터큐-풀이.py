import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

case = int(input())

for i in range(case):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = [(i, idx) for idx, i in enumerate(arr)]
    cnt = 0

    while True:
        if arr[0][0] == max(arr, key=lambda x: x[0])[0]:
            cnt += 1
            if arr[0][1] == m:
                print(cnt)
                break
            else:
                arr.pop(0)
        else:
            arr.append(arr.pop(0))
