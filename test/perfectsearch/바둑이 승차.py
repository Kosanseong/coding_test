import sys
sys.stdin = open("input.txt", "r")
# cut edge tech

def DFS(L, sum, tsum):
    global result
    if sum+(total-tsum) < result: # tsum은 나머지 애들을 구해야하니 거쳐간 노드의 모든 값을 더해준다. 그보다 하위 노드의 값들은 ()의 값
        return
    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum
    else:
        DFS(L+1, sum+a[L], tsum + a[L])
        DFS(L+1, sum, tsum + a[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    a = [0]*n
    result = -2147000000
    for i in range(n):
        a[i] = int(input())
    total = sum(a)
    DFS(0, 0)
    print(result)
