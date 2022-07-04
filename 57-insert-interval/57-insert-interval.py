class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new = []
        i = 0
        
        while i < len(intervals) :
            if intervals[i][0] >= newInterval[0]:
                break
            i += 1
        
        for j in range(i):
            new.append(intervals[j])
        
            
        new.append(newInterval)
        
        for j in range(i, len(intervals)):
            new.append(intervals[j])
        
        an = []
        
        index1 = 0
        
        while index1 < len(new):
            an.append(new[index1])
            mx = new[index1][1]
            while index1 + 1 < len(new) and \
                (new[index1+1][0] <= mx <= new[index1+1][1] or an[-1][0] <= new[index1+1][0] <= mx):
                mx = max(mx, new[index1+1][1])
                index1 += 1
            an[-1][1] = mx
            index1 += 1
        
        # print(new, an)
        return an