import sys
sys.stdin = open("input.txt", "rt")
# Union-Find 와 동일
v, e = map(int, sys.stdin.readline().split()) # 노드 수
ch = [0] * (v + 1) # 부모 행 초기화
# 부모 행 자기자신으로 설정
for n in range(1, v + 1):
    ch[n] = n

def find(ch, x):
    if ch[x] == x:
        return x
    ch[x] = find(ch, ch[x])
    return ch[x]

def union(ch, a, b):
    a = find(ch, a)
    b = find(ch, b)
    if a < b:
        ch[b] = a
    else:
        ch[a] = b

# 간선 정보
edges = []
total_cost = 0

for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))
# 거리 기준으로 오름차순 정렬
edges.sort()

for i in range(e):
    cost, a, b = edges[i]
    if (find(ch, a) != find(ch, b)):
        union(ch, a, b)
        total_cost += cost

print(total_cost)
