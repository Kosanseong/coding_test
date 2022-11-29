import sys
import heapq
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
case = int(input())

for _ in range(case):
    i = int(input())
    minHeap = []
    maxHeap = []
    index = []
    for j in range(i):
        action, num = input().split()
        if action == 'I':
            heapq.heappush(minHeap, (int(num), j))
            heapq.heappush(maxHeap, (-int(num), j))
        if action == 'D':
            if len(maxHeap) != 0 and num == '1':
                while maxHeap:
                    x = heapq.heappop(maxHeap)
                    if x[1] not in index:
                        break
                index.append(x[1])
            elif len(minHeap) != 0 and num == '-1':
                while minHeap:
                    y = heapq.heappop(minHeap)
                    if y[1] not in index:
                        break
                index.append(y[1])

    if len(minHeap) != 0:
        print(-maxHeap[0][0], minHeap[0][0])
    else:
        print("EMPTY")
