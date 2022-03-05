class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = [start]
        visited = set()
        is_valid = lambda k: 0<=k<len(arr)
        
        while queue:
            temp = []
            for i in queue:
                if i not in visited:
                    visited.add(i)
                    if arr[i] == 0:
                        return True
                    backward = i - arr[i]
                    forward = i + arr[i]
                    if is_valid(backward):
                        temp.append(backward)

                    if is_valid(forward):
                        temp.append(forward)
                
            
            queue = temp
        return False

                    
            