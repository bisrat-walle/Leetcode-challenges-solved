class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda K: K[0]**2 + K[1]**2)
 
        return points[:k]