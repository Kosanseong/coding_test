def solution(n, info):
    answer = []
    #k점을 더 많이 맞춘 사람이 점수를 가져감 (1번만)
    #둘다 0점만 맞춘 경우 그냥 0점
    #최종 점수 합산했는데 같으면 앞사람이 이김

    return answer

def dp(n,info, current):
    if n <= 0:
        return
    else:
        arrow = info[current]
        dp(n - current, info)
n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
solution(n, info)
