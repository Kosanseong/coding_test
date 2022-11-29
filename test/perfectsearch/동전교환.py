import sys

sys.stdin = open("input.txt", "r")

def DFS(L, sum):
    global res
    if L > res: # res보다 큰 레벨은 체크할 필요가 없다 왜냐 최소니까
        return
    if sum > m:
        return
    if sum == m:
        if L < res:
            res = L
    else:
        for i in coins:
            DFS(L+1, sum + i)



if __name__ == "__main__":
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    coins.sort(reverse=True)
    res = 2147000000
    DFS(0, 0)
    print(res)
