import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
sch = []
max_profit = [0] * (n+1)
for i in range(n):
    t, p = map(int, input().split())
    sch.append((t, p))

max_value = 0
for i in range(len(sch)):
    tmp = sch[i]
    max_value = max(max_value, max_profit[i])
    if tmp[0] + i <= n:
        max_profit[i + tmp[0]] = max(max_profit[i + tmp[0]], max_value + tmp[1])

print(max(max_profit))
