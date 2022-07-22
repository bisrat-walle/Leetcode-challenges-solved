class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        an = []
        for index in range(len(neg)):
            an.extend([pos[index], neg[index]])
        
        return an