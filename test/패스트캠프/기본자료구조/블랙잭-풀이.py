import sys

sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 파이썬은 1초에 2천만정도 처리 n(n-1)(n-2) / 3! 조합 식

