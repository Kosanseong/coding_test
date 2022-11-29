# 가중치 방향 그래프 (노드와 노드를 연결한 것을 간선이라 하는데 노드와 간선의 집합을 그래프라 함
# 화살표 방향이 있다면 방향 그래프라고 함
# 방향에 간선에 값까지 있다면 가중치 방향 그래프라고 함
import sys
sys.stdin = open("input.txt", "r")


n, m = map(int, input().split())
a = [[0] * n for _ in range(n)]

for i in range(m):
    n1, n2, val = map(int, input().split())
    a[n1-1][n2-1] = val

for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j], end=' ')
    print()
