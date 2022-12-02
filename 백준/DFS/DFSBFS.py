import sys
sys.stdin = open("input.txt", "r")

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n + 1)]
visited = [0] * (n+1)
for _ in range(m):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1

def DFS(v):
    visited[v] = 1
    print(v, end=' ')

    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] == 0:
            DFS(i)

def BFS(v):
    queue = [v]
    visited[v] = 0
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n + 1):
            if visited[i] == 1 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 0

DFS(v)
print()
BFS(v)
