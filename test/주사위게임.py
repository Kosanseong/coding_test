import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
res = 0

for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    print(a, b, c)

    if a==b and b==c:  #제일 높은 상금부터 걸러낸다
        money = 10000+a*1000
    elif a==b or a==c:
        money = 1000+(a*100)
    elif b == c :
        money = 1000+(b*100)
    else:
        money = c*100

    if money > res:
        res = money


print(res)
