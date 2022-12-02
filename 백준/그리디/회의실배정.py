import sys

sys.stdin = open("input.txt", "r")

n = int(input())
schedule = []
for _ in range(n):
    r, s = map(int, input().split())
    schedule.append((r, s))

schedule.sort(key=lambda x:(x[1], x[0]))
res = []
for i in schedule:
    if len(res) == 0:
        res.append(i)
    else:
        if i[0] >= res[len(res) - 1][1]:
            res.append(i)

print(len(res))
