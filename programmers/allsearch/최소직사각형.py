sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
#1. 가로세로 뒤짚는 경우

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


print(solution(sizes))
