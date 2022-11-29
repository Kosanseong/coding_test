import sys

#sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())

a = list(map(int, input().split()))

res = set()

for i in range(n):
    for j in range(i + 1, n):
        for l in range(j + 1, n):
            res.add(a[i] + a[j] + a[l])
else:
    var = list(res)
    var.sort(reverse=True)
    print(var[k-1])
