import sys

sys.stdin = open("input.txt", "r")
t = int(input())
a = [300, 60, 10]
tmp = []

for i in range(len(a)):
    cnt = t//a[i]
    tmp.append(cnt)
    if cnt != 0:
        t = t % (a[i]*cnt)

if t == 0:
    for i in range(len(tmp)):
        print(tmp[i], end=' ')
else:
    print(-1)
