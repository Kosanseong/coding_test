import sys

#sys.stdin = open("input.txt", "r")

s = input()
res = 0
cnt = 0

for x in s:
    if x.isdecimal(): # degit숫자 전체 검색, isdecimal은 0~9까지만
        res = res*10 + int(x)

for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(res, cnt)
