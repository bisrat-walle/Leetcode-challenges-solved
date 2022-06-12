class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        an = sum(nums[i] for i in range(3))
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while j < k:
                if i != j and i != k:
                    current = nums[i] + nums[j] + nums[k]
                    if abs(current-target) < abs(an-target):
                        an = current
                    if abs(an-target) == 0:
                        return an
                if current < target:
                    j += 1
                else:
                    k -= 1
        return an