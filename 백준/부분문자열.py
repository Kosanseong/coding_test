import sys
sys.stdin = open("input.txt", "rt")

a = input()
b = input()

tmp = len(a)
a = a.replace(b, "")
if tmp != len(a):
    print(1)
else:
    print(0)

