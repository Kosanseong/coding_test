import sys

sys.stdin = open("input.txt", "r")

# 그리디는 보통 정렬 문제

n = int(input())
meeting = []

for _ in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

meeting.sort(key=lambda x: (x[1], x[0])) # 주순 튜플의 1번째 차순 0번째

et = 0
cnt = 0

for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1

print(cnt)
