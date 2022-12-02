import sys

sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())
c = []
cnt = 0
for _ in range(n):
    c.append(int(input()))

c.sort(reverse=True)

for i in c:
    if k >= i:
        a = k // i
        cnt += a
        k = k % i

print(cnt)
