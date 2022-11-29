import sys

sys.stdin = open("input.txt", "r")

n, c = map(int, input().split())


def count(mid):
    cnt = 1
    ep = arr[0]

    for i in range(1, n):
        if arr[i] - ep >= mid:
            cnt += 1
            ep = arr[i]
    return cnt


arr = []
res = 0

for i in range(n):
    arr.append(int(input()))
lt = 1
rt = max(arr)

arr = sorted(arr)

while lt <= rt:
    mid = (lt + rt) // 2

    if count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt -= 1

print(res)
