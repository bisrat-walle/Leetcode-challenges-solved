class Solution:
    def tribonacci(self, n: int) -> int:
        first, second, third = 0, 1, 1
        if n == 0:
            return first
        if n == 1:
            return second
        if n == 2:
            return third
        
        for _ in range(2, n):
            first, second, third = second, third, first+second+third
            # print(first, second, third, "***")
        return third