import heapq

operations = ["I 1", "I 2", "I 3", "I 5", "I 4", "D 1"]

def solution(operations):
    heap = []
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == "I":
            heapq.heappush(heap, num)
        elif op == "D" and heap:
            if num == 1:
                heap = heapq.nlargest(len(heap), heap)[1:]
                print(heap)
                heapq.heapify(heap)
                print(heap)
            else:
                heapq.heappop(heap)

    if not heap:
        return [0, 0]

    if len(heap) == 1:
        return heap

    return [max(heap), min(heap)]

print(solution(operations))
