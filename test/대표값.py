import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))
k, index = 0, 0
l, h = float("inf"), 0
avg = round(sum(arr)/len(arr))
for i in range(n):
    m = abs(avg - arr[i])
    if m <= l :
        if arr[i] > k :
            l=m
            k, index = arr[i], i
            print(k)
print(avg, index+1)
