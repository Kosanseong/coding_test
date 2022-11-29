import sys
sys.stdin = open("input.txt", "rt")

k = int(input())
tmp = []
for _ in range(k):
    n = int(input())

    if n == 0 and tmp:
        tmp.pop()
    elif n != 0:
        tmp.append(n)


print(sum(tmp))
