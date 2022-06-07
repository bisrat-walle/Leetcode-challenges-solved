class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        di = { '2': "abc",
                '3': "def",
                '4': "ghi",
                '5': "jkl",
                '6': "mno",
                '7': "pqrs",
                '8': 'tuv',
                '9': 'wxyz'
            
        }
        if not digits:
            return []

        an = set()
        def dfs(index, st=""):
            if index >= len(digits):
                an.add(st)
                return
            
            for i in di[digits[index]]:
                dfs(index+1, st+i)
        dfs(0)
        return list(an)
            
            
            
        
        