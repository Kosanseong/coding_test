import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
m = int(input())
ch = [2147000000] * (n + 1)
arr = []

for _ in range(m):
    start, end, cost = map(int, input().split())
    arr.append((start, end, cost))

s, e = map(int, input().split())
ch[s] = 0
for i in range(n):
    for j in range(m):
        current = arr[j][0]
        next = arr[j][1]
        cost = arr[j][2]

        if ch[current] != 2147000000 and ch[next] > ch[current] + cost:
            ch[next] = ch[current] + cost

print(ch[e])
