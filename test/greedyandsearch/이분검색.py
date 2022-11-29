import sys

sys.stdin = open("input.txt", "r")

# lt와 rt를 더하여 2로 나눈 곳(중앙) 이분 검색
a, b = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
lt = 0
rt = a - 1

while lt <= rt:
    mid = (lt + rt) // 2
    if arr[mid] == b:
        print(mid + 1)
        break
    elif arr[mid] > b:
        rt = mid - 1
    else:
        lt = mid + 1




