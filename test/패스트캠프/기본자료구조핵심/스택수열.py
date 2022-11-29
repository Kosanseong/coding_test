import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
tmp = []
tmp2 = []
result = []
i = 1
for _ in range(n):
    num = int(input())

    while i <= num:
        result.append("+")
        tmp.append(i)
        i += 1

    if num == tmp[-1]:
        result.append("-")
        tmp2.append(tmp.pop())
    else:
        result.append("NO")

if "NO" in result:
    print("NO")
else:
    for i in result:
        print(i)

