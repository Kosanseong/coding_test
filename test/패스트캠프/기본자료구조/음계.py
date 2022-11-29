import sys

sys.stdin = open("input.txt", "rt")

arr = list(map(int, input().split()))
ascending = True
descending = False

for i in range(len(arr)):
    if i != (len(arr) - 1) and arr[i] == arr[i+1] - 1:
        descending = False
    elif i != (len(arr) - 1) and arr[i] == arr[i+1] + 1:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")
