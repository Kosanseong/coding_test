import sys

sys.stdin = open("input.txt", "r")

n = int(input())
a = 1000-n
arr = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in range(len(arr)):
    if a <= 0:
        break
    while a >= arr[i]:
        a -= arr[i]
        cnt += 1

print(cnt)
