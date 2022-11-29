import sys

sys.stdin = open("input.txt", "rt")

# 파이썬은 1초에 2천만정도 처리 n(n-1)(n-2) / 3! 조합 식

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr)
total = -1

for i in range(n):
    if total == m:
        break
    for j in range(i+1, n):
        for k in range(j+1, n):
            tmp = arr[i]+arr[j]+arr[k]
            if tmp > m:
                break
            total = max(total, tmp)

print(total)
