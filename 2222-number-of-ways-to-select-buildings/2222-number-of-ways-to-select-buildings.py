class Solution:
    def numberOfWays(self, s: str) -> int:
        one = zero = zero_one = one_zero = 0
        ans = 0
        for ch in s:
            if ch == "1":
                one += 1
                ans += one_zero  # "101"
                zero_one += zero
            else:
                zero += 1
                ans += zero_one # "010"
                one_zero += one
        return ans