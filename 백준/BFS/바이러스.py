import sys
from collections import deque

sys.stdin = open("input.txt", "r")

computer = int(input())
nodes = int(input())
ch = [0]*(computer+1)
queue = deque()
# 첫번째 컴퓨터부터 무조건 시작하기 때문에 1을 추가
queue.append(1)
# 이전과 다르게 2차원 배열 형식이 아닌 key,value 값으로 변경
dic = {}
for i in range(1, computer + 1):
    # 중복 값은 피하기 위하여 set 자료구조로 초기화
    dic[i] = set()

for _ in range(nodes):
    n1, n2 = map(int, input().split())
    # 양방향으로 노드가 연결된 것을 표현
    dic[n1].add(n2)
    dic[n2].add(n1)

while queue:
    # 큐에 담긴 시작 지점을 뽑아 냄
    start = queue.popleft()
    if start in dic:
        for i in dic[start]:
            # 시작 지점 키로 들어있는 밸류 중 ch[밸류] 가 0인 경우 queue에 담고 ch에 방문표시
            if ch[i] == 0:
                queue.append(i)
                ch[i] = 1

print(ch)
print(sum(ch) - 1)




