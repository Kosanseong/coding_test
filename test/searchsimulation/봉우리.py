import sys

sys.stdin = open("input.txt", "r")


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

#상하좌우 탐색시
dx = [-1, 0, 1, 0] # 두 리스트를 합치면 함수처럼 1사분면 등으로 표현 가능
dy = [0, 1, 0, -1]


a.insert(0, [0]*n)
a.append([0]*n)

for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)): #괄호 안에 조건이 모두 참일 때 참, for 뒤에는 4번 돌린다.
            cnt += 1

print(cnt)

