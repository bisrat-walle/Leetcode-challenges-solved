class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        left, right = 0, 1
        ans = 0
        while right < len(colors):
            sum_ = neededTime[left]
            mx_ = neededTime[left]
            while right < len(colors) and colors[left] == colors[right]:
                sum_ += neededTime[right]
                mx_ = max(mx_, neededTime[right])
                right += 1
            
            if sum_ != mx_:
                ans += sum_-mx_
            
            left = right
            right +=1
        
        return ans
        