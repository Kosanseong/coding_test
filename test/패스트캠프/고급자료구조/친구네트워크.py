import sys
sys.stdin = open("input.txt", "rt")

case = int(input())
# union-find 활용
def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]
        print(number[x])

for _ in range(case):
    parent = {}
    number = dict()
    f = int(input())
    d = dict()
    result = 0
    for _ in range(f):
        f1, f2 = input().split()

        if f1 not in parent:
            parent[f1] = f1
            number[f1] = 1

        if f2 not in parent:
            parent[f2] = f2
            number[f2] = 1

        union(f1, f2)

        print(number[find(f1)])









