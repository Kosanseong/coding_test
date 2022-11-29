class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def climbStairs_2(n):
            if n in cache:
                return cache[n]
            if n <= 3:
                result = n
            else:
                result = climbStairs_2(n-1) + climbStairs_2(n-2)

            cache[n] = result

            return result
        return climbStairs_2(n)


