import sys
import heapq
sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline

n = int(input())

a = []
for j in range(n):
    i = int(input())
    if i != 0:
        if i < 0:
            heapq.heappush(a, (-1 * i, i))
        else:
            heapq.heappush(a, (i, i))
    else:
        if len(a) == 0:
            print(0)
        else:
            x, origine = heapq.heappop(a)
            if origine < 0:
                print(-1 * x)
            else:
                print(x)
