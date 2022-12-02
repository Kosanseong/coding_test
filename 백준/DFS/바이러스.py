import sys
sys.stdin = open("input.txt", "r")

n = int(input())
m = int(input())
arr = [[]*(n + 1) for _ in range(n + 1)]
ch = [0] * (n + 1) # 01234567
cnt = 0

for _ in range(m):
    m1, m2 = map(int, input().split())
    arr[m1].append(m2)
    arr[m2].append(m1)

def DFS(L):
    global cnt
    ch[L] = 1

    for i in arr[L]:
        if ch[i] == 0:
            cnt += 1
            DFS(i)

DFS(1)
print(cnt)

