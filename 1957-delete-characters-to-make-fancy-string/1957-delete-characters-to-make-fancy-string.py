class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for ch in s:
            stack.append(ch)
            while len(stack) > 2 and stack[-1] == stack[-2] == stack[-3]:
                stack.pop()
        return "".join(stack)