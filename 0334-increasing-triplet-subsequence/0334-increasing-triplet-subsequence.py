class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        one, two = float("inf"), float("inf")
        for num in nums:
            if num <= one:
                one = num
            elif num <= two:
                two = num
            else:
                return True
        return False