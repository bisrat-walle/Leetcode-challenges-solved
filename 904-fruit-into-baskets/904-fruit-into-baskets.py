class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        di, left, right = {}, 0, 0
        mx = None
        while(right < len(fruits)):
        
            if fruits[right] in di.keys():
                di[fruits[right]] += 1
            else:
                di[fruits[right]] = 1

            while len(di) > 2:
                if di[fruits[left]] == 1:
                    del di[fruits[left]]
                else:
                    di[fruits[left]] -= 1
                
                left += 1
            

            if not mx:
                mx = right-left+1
            else:
                mx = max(mx, right-left+1)
            right += 1
        
        return mx