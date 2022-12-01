import sys
#input.txt -> 3,4,7,10
sys.stdin = open("input.txt", "r")
case = int(input())

def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    return dp(n-1) + dp(n-2) + dp(n-3)

for _ in range(case):
    n = int(input())
    print(dp(n))

# n = 4 일 때부터 현재 숫자보다 3적은 수의 경우의 수부터 1작은 수의 경우의 수까지 더한 것이 현재수의 경우의 수가된다.
# ex) 7의 경우의 수 -> 6의 경우의 수 + 5의 경우의 수 + 4의 경우의 수

