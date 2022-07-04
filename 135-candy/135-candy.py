class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies_right = [1] * len(ratings)
        candies_left = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies_right[i] = candies_right[i-1] + 1
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies_left[i] = candies_left[i+1] + 1
                
        return sum(map(max, zip(candies_right, candies_left)))