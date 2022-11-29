import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
ch = [0] * (n+1)
for _ in range(m):
    l1, l2 = map(int, input().split())
    arr[l1].append(l2)
    arr[l2].append(l1)

print(arr)
cnt = 0
def DFS(v):
    ch[v] = 1
    for i in arr[v]:
        print(i)
        if ch[i] == 0:
            DFS(i)
DFS(1)
print(sum(ch) - 1)

# 핵심은 l1과 l2에 l2와 l1을 각각 연결
