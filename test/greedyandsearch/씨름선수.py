import sys

sys.stdin = open("input.txt", "r")

n = int(input())
arr = []

for _ in range(n):
    h, w = map(int, input().split())
    arr.append((h, w))

arr.sort(reverse=True)
count = 0
largest = 0

for x, y in arr:
    if y > largest:
        largest = y
        count += 1

print(count)
