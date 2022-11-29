import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
ch = [0] * (n + 1)
cnt = 0

for i in range(2, n + 1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n + 1, i):
            ch[j] = 1

print(cnt)
'''
내 풀이
set = set()

for i in range(2, n+1):
    for j in range(2, i):
        if i % j != 0:
            set.add(i)
            print(i)
print(len(set))
'''

arr = [1, 1, 1, 1, 3, 4, 6]
answer = []

answer = set(arr)
list(answer)
print(answer)
