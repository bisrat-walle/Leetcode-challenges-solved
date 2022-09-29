from heapq import *

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            heappush(heap, (abs(num-x), num))
        ans = []
        dif = None
        while len(ans) < k:
            dif, value = heappop(heap)
            ans.append(value)
        if heap and dif == heap[0][0]:
            ans[-1] = min(ans[-1], heap[0][1])
        ans.sort()
        return ans