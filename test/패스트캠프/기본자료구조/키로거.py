import sys
sys.stdin = open("input.txt", "rt")

case = int(input())

for _ in range(case):
    action = input()
    result = []
    tmp = []
    for i in action:
        if i == "<":
            if result:
                tmp.append(result.pop())
        elif i == ">":
            if tmp:
                result.append(tmp.pop())
        elif i == "-":
            if result:
                result.pop()
        else:
            result.append(i)
    while tmp:
        result.append(tmp.pop())

    for i in result:
        print(i, end='')
    print()
