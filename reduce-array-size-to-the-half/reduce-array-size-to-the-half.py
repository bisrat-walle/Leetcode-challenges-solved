class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        di = {}
        for i in arr:
            if i not in di.keys():
                di[i] = 1
            else:
                di[i] += 1
        l = len(arr)
        m = 0
        n = 0
        for i, j in sorted(di.items(),key=lambda x: x[1], reverse=True):
            if m >= l//2:
                break
            n += 1
            m += j
        return n
                