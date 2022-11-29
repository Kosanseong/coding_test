import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
tmp = []
for _ in range(n):
    command = input().split()
    if len(command) == 2:
        if command[0] == "push":
            tmp.append(int(command[1]))
    else:
        if command[0] == "top" and tmp:
            print(tmp[len(tmp)-1])
        elif command[0] == "size":
            print(len(tmp))
        elif command[0] == "empty":
            if tmp:
                print(0)
            else:
                print(1)
        elif command[0] == "pop" and tmp:
            print(tmp.pop())
        else:
            print(-1)

