class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        an = []
        for i in range(len(l)):
            current = nums[l[i]:r[i]+1]
            current.sort()
            n = len(current)
            if n <= 1:
                an.append(True)
            else:
                d = current[1]-current[0]
                for j in range(1, n):
                    if current[j] - current[j-1] != d:
                        an.append(False)
                        break
                else:
                    an.append(True)
        return an