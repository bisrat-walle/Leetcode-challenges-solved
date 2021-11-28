class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size = len(nums1) + len(nums2)
        mid = size//2
        nums1.extend(nums2)
        mylist = sorted(nums1)

        if size % 2 == 0:
            return (mylist[mid]+mylist[mid-1])/2
        return  mylist[mid]
                
            