import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))
result = list()


def isPrime(x):
    if x == 1:
        return False  # 1이면 안된다.

    for j in range(2, x // 2 + 1):  # 절반까지만 확인하면 된다.
        if x % j == 0:
            return False
    else:
        return True

def toReverseNumber(x):
    res = 0

    while x > 0:
        t = x % 10
        x = x // 10

        res = res * 10 + t

    return res


for i in arr:
    reversedNumber = toReverseNumber(i)

    if isPrime(reversedNumber):
        result.append(reversedNumber)

print(result)
