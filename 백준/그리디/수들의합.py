import sys

sys.stdin = open("input.txt", "r")
s = int(input())

res = 0
i = 0
while True:
    if res == s:
        break
    elif res > s:
        tmp = res - s
        if tmp <= i:
            i -= 1
            break

    i += 1
    res += i

print(i)

