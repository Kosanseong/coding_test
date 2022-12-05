import sys
from collections import deque

sys.stdin = open("input.txt", "r")

computer = int(input())
nodes = int(input())
ch = [0]*(computer+1)
queue = deque()
queue.append(1)
dic = {}
for i in range(1, computer + 1):
    dic[i] = set()

for _ in range(nodes):
    n1, n2 = map(int, input().split())
    dic[n1].add(n2)
    dic[n2].add(n1)

while queue:
    start = queue.popleft()
    if start in dic:
        for i in dic[start]:
            if ch[i] == 0:
                queue.append(i)
                ch[i] = 1

print(ch)
print(sum(ch) - 1)




