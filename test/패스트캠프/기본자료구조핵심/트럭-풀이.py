import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

n, w, L = map(int, input().split())

a = list(map(int, input().split()))
tmp = deque([0] * w)
d = deque(a)


