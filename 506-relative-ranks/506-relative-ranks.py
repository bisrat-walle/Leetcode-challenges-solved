class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = [i for i in score]
        temp.sort(reverse=True)
        rank = {}
        for r, val in enumerate(temp):
            rank[val] = r+1
        an = []
        for i in score:
            if rank[i] == 1:
                an.append("Gold Medal")
            elif rank[i] == 2:
                an.append("Silver Medal")
            elif rank[i] == 3:
                an.append("Bronze Medal")
            else:
                an.append(str(rank[i]))
        
        return an
        