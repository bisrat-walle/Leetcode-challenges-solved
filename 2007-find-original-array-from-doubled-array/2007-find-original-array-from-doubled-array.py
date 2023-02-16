class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = Counter(changed)
        ans = []
        for num in sorted(changed):
            if counter[num]:
                if (num ==  0 and counter[0] < 2) or counter[2 * num] == 0:
                    return []
                counter[num] -= 1
                counter[2 * num] -= 1
                ans.append(num)
        return ans