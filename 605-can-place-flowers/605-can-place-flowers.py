class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return flowerbed[0] == 0
        max_planted, i, ln = 0 , 0, len(flowerbed)
        while i < ln:
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] != 1:
                    flowerbed[i] = 1
                    max_planted += 1
                i += 1
                continue
            if i == ln-1:
                if flowerbed[i] == 0 and flowerbed[i-1] != 1:
                    flowerbed[i] = 1
                    max_planted += 1
                i += 1
                continue
            if flowerbed[i] == 0 and flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                flowerbed[i] = 1
                max_planted += 1
                i += 1
            else:
                i += 1
        
        # print(max_planted)
        
        return max_planted >= n
                
            