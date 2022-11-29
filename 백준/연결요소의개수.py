import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
n, m = map(int, input().split())
ch = [0] * (n + 1)
cnt = 0
line = {}
for _ in range(m):
    l1, l2 = map(int, input().split())
    if l1 not in line:
        line[l1] = [l2]
    else:
        line[l1].append(l2)

def DFS(start):
    ch[start] = 1
    for i in line[start]:
        if i in line and ch[i] == 0:
            DFS(i)

for i in line.keys():
    if ch[i] == 0:
        DFS(i)
        cnt += 1

print(cnt)

