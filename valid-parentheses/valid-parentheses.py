class Solution:
    def isValid(self, s: str) -> bool:
        dc = { '(': ')',
              '{': '}',
              '[' : ']'
            
        }
        stack = []
        for i in s:
            if i in dc.keys():
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                op = stack.pop()
                
                if dc[op] != i:
                    return False
        if len(stack) != 0:
            return False
        return True
                    