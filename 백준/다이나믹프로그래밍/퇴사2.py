import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
sch = []
# 각 날이 끝나는 기준이라면 그 날의 최대 임금 값을 저장하기 위한 배열
max_profit = [0] * (n+1)
for i in range(n):
    t, p = map(int, input().split())
    sch.append((t, p))

# 현재 가장 높은 임금이 얼마인지 체크
max_value = 0
for i in range(len(sch)):
    tmp = sch[i]
    # 현재 맥스 밸류와 현재 스케쥴이 끝나는 날의 맥스밸류와 비교하여 업데이트
    max_value = max(max_value, max_profit[i])
    '''
    현재 날짜와 그 날짜에 잡혀있는 스케쥴이 끝나는 날이 n보다 작을 경우
    끝나는 날 인덱스에 기존에 끝나는 날 인덱스에 있던 값과 현재 값과 맥스 밸류를 비교하여 맥스를 저장
    n을 넘어가면 고려할 이유가 없기 때문에 제거
    '''
    if tmp[0] + i <= n:
        max_profit[i + tmp[0]] = max(max_profit[i + tmp[0]], max_value + tmp[1])

# 최대 임금 배열에서 제일 큰 값을 출력
print(max(max_profit))
