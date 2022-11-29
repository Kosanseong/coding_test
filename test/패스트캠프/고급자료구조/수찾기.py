import sys
import hashlib
sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
tmp = dict()
for i in a:
    tmp[i] = 1

for i in b:
    if i in tmp:
        print(1)
    else:
        print(0)

