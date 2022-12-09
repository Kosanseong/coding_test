import sys
sys.stdin = open("input.txt", "rt")
n, s = map(int, input().split())

arr = list(map(int, input().split()))
lt = 0
rt = 0
res = 2147000000
tmp = 0

while True:
    if tmp >= s:
        res = min(res, rt - lt)
        tmp -= arr[lt]
        lt += 1
    else:
        if rt == n:
            break
        tmp += arr[rt]
        rt += 1

if res == 2147000000:
    print(0)
else:
    print(res)

