import sys

sys.stdin = open("input.txt", "r")

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
tmp = []
res = 0

while a:
    tmp.append((min(a), max(b)))
    a.remove(min(a))
    b.pop(b.index(max(b)))

for i in tmp:
    res += i[0]*i[1]

print(res)





