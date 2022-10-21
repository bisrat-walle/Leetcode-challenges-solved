class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexes = defaultdict(list)
        for index in range(len(nums)):
            num = nums[index]
            indexes[num].append(index)
            if len(indexes[num]) > 1 and abs(indexes[num][-1]-indexes[num][-2]) <= k:
                return True
        return False