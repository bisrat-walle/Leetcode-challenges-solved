class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        cur_sum = 0
        heap = []
        ans = float('-inf')
        arr = sorted(zip(efficiency, speed),reverse=True)
        for i, j in arr:
            while len(heap) > k-1:
                cur_sum -= heappop(heap)
                
            heappush(heap, j)
            cur_sum += j
            ans = max(ans, cur_sum * i)
            
        return ans % (10**9+7)