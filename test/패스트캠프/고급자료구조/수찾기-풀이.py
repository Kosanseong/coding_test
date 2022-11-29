import sys
import hashlib
sys.stdin = open("input.txt", "rt")

# set은 어떤 집합을 찾을 때 보통 쓰인다. set은 해시가 있다.

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for i in b:
    if i not in a:
        print(0)
    else:
        print(1)
