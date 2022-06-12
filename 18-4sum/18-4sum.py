class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        an = set()
        for i in range(n):
            for j in range(i, n):
                    a, b = j+1, n-1
                    while a < b:
                        current = nums[i]+nums[j]+nums[a]+nums[b]
                        tp = [nums[i],nums[j],nums[a],nums[b]]
                        tp.sort()
                        if current == target and (i != j != a != b):
                            if tuple(tp) not in an:
                                an.add(tuple(tp))
                        # print(tp, current)
                        if current < target:
                            a += 1
                        else:
                            b -= 1
        return list(map(list, list(an)))
        