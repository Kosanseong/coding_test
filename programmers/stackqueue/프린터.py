from collections import deque
priorities = [2, 1, 3, 2]
location = 2


def solution(priorities, location):
    answer = 0
    d = deque(priorities)
    temp = deque([x for x in range(len(d))])
    while d:
        p = d.popleft()
        if d:
            if p < max(d):
                temp.append(temp.popleft())
                print(temp)
                d.append(p)
            else:
                answer += 1
                if temp[0] == location:
                    return answer
                else:
                    temp.popleft()

    return answer + 1


print(solution(priorities, location))
