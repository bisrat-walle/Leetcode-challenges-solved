class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = len(nums2)
        an = []
        for i in nums1:
            index = nums2.index(i)
            for j in range(index+1, l):
                if nums2[j] > i:
                    an.append(nums2[j])
                    break
            else:
                an.append(-1)
        return an
    
    
    