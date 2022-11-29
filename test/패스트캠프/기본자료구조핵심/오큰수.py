import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

a = list(map(int, input().split()))
stack = [] #스택 초기화
NGE = [-1]* n # 오큰수 배열


for i in range(n):
    x = a[i] # 하나씩 수확인
    if len(stack) == 0 or stack[-1][0] >= x:
        stack.append((x, i))
    else:
        while len(stack) > 0:
            previous, index = stack.pop()
            if previous >= x: # 크거나 같은 이전 원소를 만났다면 다시 삽입
                stack.append((previous, index))
                break
            else:
                NGE[index] = x # 오큰수 기록
        stack.append((x, i)) # (수, 인덱스) 형태로 삽입

for x in NGE:
    print(x, end=' ')


