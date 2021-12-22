class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack= []
        for i in range(len(s)):
            if s[i] == ')':
               temp_stack = []
               while stack[-1] != '(':
                    temp_stack.append(stack.pop())
               stack.pop()
               for i in temp_stack:
                    stack.append(i)
            else:
               stack.append(s[i])
        return ''.join(stack)
    