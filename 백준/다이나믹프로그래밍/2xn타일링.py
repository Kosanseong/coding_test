import sys

sys.stdin = open("input.txt", "r")
'''
2xn 타일에 2x1타일을 넣는 경우의 수는 n-1번째 방법과 n-2번째 경우의 수를 합해주면 된다.
'''

n = int(input())
dp = [0] * (n + 1)

'''
n == 1 일 때, 2번 인덱스가 없기 때문에,
dp[2]가 없다 따라서 index error 가 발생하기 때문에 
n == 1 일땐 바로 프린트 해주고 마무리한다.
'''
if n == 1:
    print(1)
else:
    dp[1] = 1
    dp[2] = 2
    '''
    bottom-up 방식
    '''
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n] % 10007)

    '''
    top-down 방식
    '''
    def DFS(n):
        if dp[n] != 0:
            return dp[n]

        return DFS(n-1) + DFS(n-2)

    print(DFS(n) % 10007)
