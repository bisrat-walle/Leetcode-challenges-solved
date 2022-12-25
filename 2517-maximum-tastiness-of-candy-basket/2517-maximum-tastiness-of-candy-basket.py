class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)
        left = 0
        right = price[n-1] - price[0]
        while left < right:
            mid = (left+right+1)//2
            cnt = 1
            prev = price[0]
            for i in range(1, n):
                if price[i] - prev >= mid:
                    cnt += 1
                    prev = price[i]
            if cnt >= k:
                left = mid
            else:
                right = mid-1
        
        return left