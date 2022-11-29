import sys
sys.stdin = open("input.txt", "rt")

tmp = []
for i in range(5):
    att = list(map(int, input().split()))
    tmp.append((i+1, sum(att)))

winner = max(tmp, key=lambda x: x[1])
print(winner[0], winner[1])
