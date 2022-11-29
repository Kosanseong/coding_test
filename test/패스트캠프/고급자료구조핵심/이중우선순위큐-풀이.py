import sys
import heapq
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
case = int(input())
def pop(heap):
    while heap:
        data, id = heapq.heappop(heap)
        if not deleted[id]:
            deleted[id] = True
            return data
    return None

for _ in range(case):
    i = int(input())
    minHeap = []
    maxHeap = []
    current = 0
    deleted = [False] * (i+1)
    for j in range(i):
        command = input().split()
        operator, data = command[0], int(command[1])
        if operator == 'D':
            if data == -1: pop(minHeap)
            elif data == 1: pop(maxHeap)
        elif operator == 'I':
            heapq.heappush(minHeap, (data, current))
            heapq.heappush(maxHeap, (-data, current))
            current += 1

    max_value = pop(maxHeap)
    if max_value == None: print("EMPTY")
    else:
        heapq.heappush(minHeap, (-max_value, current))
        print(-max_value, pop(minHeap))




