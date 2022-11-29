import sys

sys.stdin = open("input.txt", "r")
n = int(input())
s = input()
res = 0
for i in range(len(s)):
    res += int(s[i])

print(res)
