class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        arr = [[*tasks[i], i] for i in range(n)]
        arr.sort()
        ans = []
        heap = []
        current = 0
        ptr = 0
        while ptr < n:
            current = max(current, arr[ptr][0])
            while ptr < n and arr[ptr][0] <= current:
                heappush(heap, (arr[ptr][1], arr[ptr][2]))
                ptr += 1
            
            while heap and (ptr >= n or arr[ptr][0] > current):
                duration, idx = heappop(heap)
                ans.append(idx)
                current += duration
        
        return ans