progresses = [93, 30, 55]
speeds = [1, 30, 5]
def solution(progresses, speeds):
    answer = []
    cnt = 0
    cnt2 = 0
    for i in range(len(progresses)):
        tmp = progresses[i] + (speeds[i] * cnt)
        if i != 0 and tmp < 100:
            answer.append(cnt2)
            cnt2 = 0

        while tmp < 100:
            tmp += speeds[i]
            cnt += 1

        cnt2 += 1

    answer.append(cnt2)
    return answer

print(solution(progresses, speeds))
