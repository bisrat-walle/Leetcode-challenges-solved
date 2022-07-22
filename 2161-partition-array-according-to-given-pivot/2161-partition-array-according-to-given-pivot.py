class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessthan = []
        greaterthan = []
        equal = []
        for current in nums:
            if current < pivot:
                lessthan.append(current)
            elif current == pivot:
                equal.append(current)
            else:
                greaterthan.append(current)
        lessthan.extend(equal)
        lessthan.extend(greaterthan)
        return lessthan