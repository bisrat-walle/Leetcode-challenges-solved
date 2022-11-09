class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def rec(current, index):
            if index >= len(s):
                ans.append(current)
                return
            if not current[index].isalpha():
                rec(current, index+1)
            else:
                rec(current[:index]+current[index].lower()+current[index+1:], index+1)
                rec(current[:index]+current[index].upper()+current[index+1:], index+1)
        
        rec(s, 0)
        
        return ans