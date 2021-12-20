class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i == '+':
                result = int(stack.pop())+int(stack.pop())
                stack.append(result)
            elif i == '-':
                last = int(stack.pop())
                result = int(stack.pop()) - last
                stack.append(result)
            elif i == '*':
                result = int(stack.pop())*int(stack.pop())
                stack.append(result)
            elif i == '/':
                last = int(stack.pop())
                result = int(int(stack.pop()) / last)
                stack.append(result)
            else:
                stack.append(i)
        return stack.pop()