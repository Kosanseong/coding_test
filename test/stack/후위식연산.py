import sys

sys.stdin = open("input.txt", "r")

a = input()
stack = []

for i in a:
    if i.isdecimal():
        stack.append(i)
    elif i == '+':
        stack.append(int(stack.pop()) + int(stack.pop()))
    elif i == '-':
        stack.append(-int(stack.pop()) + int(stack.pop()))
    elif i == '*':
        stack.append(int(stack.pop()) * int(stack.pop()))
    elif i == '/':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2 / n1)

print(stack)


