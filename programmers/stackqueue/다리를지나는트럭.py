from collections import deque
truck_weights = [7,4,5,6]
bridge_length = 2
weight = 10


def solution(bridge_length, weight, truck_weights):
    passing = deque([0 for _ in range(bridge_length)])
    second = 0
    currentWeightOnBridge = 0
    trucks = deque(truck_weights)

    while trucks or currentWeightOnBridge > 0:
        removedWeight = passing.popleft()
        currentWeightOnBridge -= removedWeight

        if trucks and currentWeightOnBridge + trucks[0] <= weight:
            tmp = trucks.popleft()
            passing.append(tmp)
            currentWeightOnBridge += tmp
        else:
            passing.append(0)

        second += 1

    return second


print(solution(bridge_length, weight, truck_weights))
