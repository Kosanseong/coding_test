import sys

sys.stdin = open("input.txt", "rt")

n = int(input())

arr = list(map(int, input().split()))

#파이썬 편한 방법이라는데 형변환을 두번하는데 애초에 받을 때 인트로 안받으면 되는 것이 아닌가?
def digit_sum(x):
    sum=0
    for i in str(x): #i는문자열에 문자하나하나
        sum += int(i)

    return sum




'''
def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum


max = -2147000000

for i in arr:
    tot = digit_sum(i)
    if tot > max:
        max = tot
        res = i

print(res)
'''


'''
tmp, number = 0, 0

compare = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
       compare += int(arr[i][j])
    if compare > tmp:
        tmp, number = compare, int(arr[i])
        compare = 0
print(number)
'''
