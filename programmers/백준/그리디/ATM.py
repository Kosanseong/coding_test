import sys

sys.stdin = open("input.txt", "r")

n = int(input())
p = list(map(int, input().split()))
res = []

p.sort()
for i in range(len(p)):
    res.append(sum(p[:i+1]))

print(sum(res))


