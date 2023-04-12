class Solution:
    def splitString(self, s: str) -> bool:
        """
        1234
        
        [12,34]
        
        """
        
        path = []
        ans = False
        
        def backtrack(index):
            nonlocal ans
            # print(path, index)
            if index >= len(s):
                if len(path) > 1:
                    ans = True
                return
            for ln in range(1, (len(s)-index)+1):
                if len(path) == 0:
                    path.append(int(s[index:index+ln]))
                    backtrack(index+ln)
                    path.pop()
                elif (path[-1] - 1) == int(s[index:index+ln]):
                    path.append(int(s[index:index+ln]))
                    backtrack(index+ln)
                    path.pop()
                    
        backtrack(0)         
                    
        return ans