arr = [1, 1, 3, 3, 0, 1, 1]
arr2 = [4, 4, 4, 3, 3]


def solution(arr):
    answer = list()
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        else:
            if arr[i] != arr[i-1]:
                answer.append(arr[i])

    return answer

print(solution(arr2))
