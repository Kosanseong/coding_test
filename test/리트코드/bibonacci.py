class Solution:
    def fib(self, n: int) -> int:
        a = []
        for i in range(n+1):
            if i == 0:
                a.append(0)
            elif i == 1:
                a.append(1)
            else:
                a.append(a[i-1] + a[i-2])
        return a[-1]


print(Solution.fib(Solution, 0))
