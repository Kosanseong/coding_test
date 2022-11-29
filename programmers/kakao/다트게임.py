from collections import deque
# 다트 3차례 합산
# 0~10
# SDT 제곱 3제곱
# *상은 해당점수 바로전 얻은 점수 2배
# #상은 점수 -
# 중첩 * 당 4배
# 처음 *이면 그럼 처음 스타상에서만 점수 2
# *#이면 - 2배


def solution(dartResult):
    answer = 0
    res = []
    a = deque()
    for i in range(len(dartResult)):
        a.append(dartResult[i])

    while a:
        i = a.popleft()
        if str(i).isdecimal():
            ai = a.popleft()
            if i == '1' and ai == '0':
                res.append(10)
            else:
                res.append(int(i))
                a.insert(0, ai)

        if i == '*':
            if len(res) == 1:
                res[0] = res[0] * 2
            else:
                tmp = res.pop()
                tmp1 = res.pop()
                res.append(tmp1 * 2)
                res.append(tmp * 2)

        elif i == '#':
            tmp = res.pop()
            res.append(tmp * (-1))

        if i == 'S':
            res.append(int(res.pop()))
        elif i == 'D':
            res.append(int(res.pop())**2)
        elif i == 'T':
            res.append(int(res.pop())**3)

    answer = sum(res)
    return answer



print(solution("1D2S#10S"))
