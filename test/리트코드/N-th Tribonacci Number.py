class Solution:
    def tribonacci(self, n: int) -> int:
        a = []
        for i in range(n+1):
            if i == 0:
                a.append(0)
            elif i == 1 or i == 2:
                a.append(1)
            else:
                a.append(a[i-1] + a[i-2] + a[i-3])

        return a[-1]


print(Solution.tribonacci(Solution, 4))
