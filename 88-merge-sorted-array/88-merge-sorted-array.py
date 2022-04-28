class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i, j = 0, 0
        temp = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        
        while i < m:
            temp.append(nums1[i])
            i += 1
        
        while j < n:
            temp.append(nums2[j])
            j += 1
        # print(temp)
        for i in range(len(nums1)):
            nums1[i] = temp[i]
        