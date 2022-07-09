class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        index = 1
        pos = 1
        consecative_counter = 1
        while index < len(nums):
            if nums[index] == nums[index-1]:
                if consecative_counter < 2:
                    nums[pos] = nums[index]
                    pos += 1
                consecative_counter += 1
            else:
                consecative_counter = 1
                nums[pos] = nums[index]
                pos += 1
            index += 1
            # print(index, pos)
        k = pos
        for _ in range(len(nums)-k):
            nums.pop()
        return k