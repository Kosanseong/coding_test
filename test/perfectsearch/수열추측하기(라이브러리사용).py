import sys
import itertools as it  # 순열을 구할 수 있는 라이브러리

sys.stdin = open("input.txt", "r")
n, f = map(int, input().split())
b = [1] * n
for i in range(1, n):
    b[i] = b[i - 1] * (n - i) / i

a = list(range(1, n + 1))
for tmp in it.permutations(a):  # 이렇게하면 a에 배열에 3가지를 뽑아 만든 리스트
    sum = 0
    for L, x in enumerate(tmp):
        sum += x * b[L]
    if sum == f:
        print(tmp)
        break
