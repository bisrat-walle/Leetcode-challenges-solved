class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        op = 0
        di = {}
        for i in nums:
            if (k-i) not in di.keys():
                if i not in di.keys():
                    di[i] = 1
                else:
                    di[i] += 1
            else:
                if di[k-i] == 0:
                    if i not in di.keys():
                        di[i] = 1
                    else:
                        di[i] += 1
                else:
                    di[k-i] -= 1
                    op += 1
        return op
                    
            