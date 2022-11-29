import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

arr = list(map(int, input().split()))

def count(mid):
    cnt = 1
    sum = 0
    for x in arr:
        if sum + x > mid:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt
lt = 1
rt = sum(arr)
res = 0
maxx = max(arr)

while lt <= rt:
    mid = (lt+rt) // 2

    if mid >= maxx and count(mid) <= m:
        res = mid
        rt = mid-1
    else:
        lt = mid + 1

print(res)
