class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            stack.append(ch)
            while len(stack) > 2 and stack[-1] == "c" and stack[-2] == "b" and \
                stack[-3] == "a":
                for _ in range(3):
                    stack.pop()
        return stack == []