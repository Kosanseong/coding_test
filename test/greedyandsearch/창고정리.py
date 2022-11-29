import sys

sys.stdin = open("input.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

for i in range(m):
    arr.sort(reverse=True)
    arr[0] -= 1
    arr[n-1] += 1

print(max(arr) - min(arr))
