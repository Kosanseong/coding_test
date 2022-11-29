import sys
#K번째 약수 찾기
#sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
cnt = 0
for x in range(1, n + 1):  # 이래야 n까지 돈다
    if n % x == 0:
        cnt += 1
    if cnt == k:
        print(x)
        break
else:
    print(-1)
