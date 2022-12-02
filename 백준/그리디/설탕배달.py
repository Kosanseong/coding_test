import sys

sys.stdin = open("input.txt", "r")

w = int(input())
cnt = 0
while True:
    if w < 0:
        cnt = -1
        break
    if w % 5 == 0:
        cnt += w // 5
        break
    else:
        w -= 3
        cnt += 1

print(cnt)


