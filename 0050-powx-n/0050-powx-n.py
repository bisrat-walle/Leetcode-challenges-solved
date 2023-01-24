class Solution:
    def myPow(self, x: float, n: int) -> float:
        pos = n > -1
        n = abs(n)
        def solve(x, n):
            if not n:
                return 1
            if n==1:
                return x
            half = n//2
            temp = solve(x, half)
            return temp*(temp if n%2 == 0 else temp*x)
        res = solve(x, n)
        return res if pos else 1/res