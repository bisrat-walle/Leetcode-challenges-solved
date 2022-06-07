class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        possible_comb = []
        @lru_cache(None)
        def dfs(op, cl, current=""):
            if op == 0 and cl == 0:
                possible_comb.append(current)
            if cl == 0:
                return
            if op != 0:
                dfs(op-1, cl, current+"(")
            if cl != 0:
                dfs(op, cl-1, current+")")
        
        def is_valid(st):
            stack = []
            for i in st:
                if i == "(":
                    stack.append(i)
                elif not stack:
                    return False
                else:
                    stack.pop()
            return stack == []
        
        dfs(n, n)
        an = []
        
        for st in possible_comb:
            if is_valid(st):
                an.append(st)
        return an
                    