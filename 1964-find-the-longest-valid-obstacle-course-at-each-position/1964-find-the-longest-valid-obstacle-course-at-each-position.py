class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        ans = [1 for i in range(n)]
        arr = []
        for i in range(n):
            left, right = 0, len(arr) - 1
            current = obstacles[i]
            best = -1
            while left <= right:
                mid = (left + right)//2
                if arr[mid] > current:
                    best = mid
                    right = mid-1
                else:
                    left = mid+1
                    
            if best == -1:
                arr.append(current)
                ans[i] = len(arr)
            else:
                arr[best] = min(arr[best], current)
                ans[i] = best + 1
                
        
        return ans