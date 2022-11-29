import sys

sys.stdin = open("input.txt", "r")


# 각 줄에는 각 인덱스 + 1 만큼을 들어올릴 수 있으니 각 계산하고 비교하면됨
n = int(input())
a = [(int(input())) for _ in range(n)]
tmp = []
a.sort(reverse=True)

for i in range(len(a)):
    tmp.append(a[i] * (i+1))

print(max(tmp))
