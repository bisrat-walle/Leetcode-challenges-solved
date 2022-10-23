class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            if not b:
                return a
            return gcd(b, a%b)
        return gcd(min(nums), max(nums))
    