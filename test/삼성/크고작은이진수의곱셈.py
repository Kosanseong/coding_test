import sys
sys.stdin = open("input.txt", "rt")

case = int(input())

def max(a, b):
    str = ''
    for i in range(a):
        str += '1'

    for i in range(b):
        str += '0'

    return int(str, 2)

def min(a, b):
    str = '1'
    for i in range(b):
        str += '0'

    for i in range(a-1):
        str += '1'

    return int(str, 2)

for i in range(case):
    a, b = map(int, input().split())
    max_val = max(a, b)
    min_val = min(a, b)
    multiple = bin(max_val * min_val)[2:]

    print("#", end='')
    print(i+1, end=' ')
    print(multiple.count('1'))

