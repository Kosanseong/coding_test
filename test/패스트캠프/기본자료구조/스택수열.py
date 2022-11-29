import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
arr = [int(input()) for _ in range(n)]
tmp = []
answer = []
i = 1
while arr:
    if i == n+2:
        answer.append("NO")
        break
    if len(tmp) != 0 and tmp[len(tmp) - 1] == arr[0]:
        tmp.pop()
        arr.pop(0)
        answer.append("-")
    else:
        answer.append("+")
        tmp.append(i)
        i += 1

if answer.__contains__("NO"):
    print("NO")
else:
    for i in answer:
        print(i)


