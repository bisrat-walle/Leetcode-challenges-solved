class Solution:
    def decodeString(self, s: str) -> str:
            digits = ["0", "1", "2", "3", "4", "5","6", "7", "8", "9"]
            stack = []
            for i in s:
                if i == "]":
                    temp = []
                    while stack and stack[-1] != "[":
                        temp.insert(0, stack.pop())
                    if stack:
                        stack.pop()
                    rep = ""
                    while stack and stack[-1] in digits:
                        rep = stack[-1] + rep
                        stack.pop()
                    if rep != "":
                        for i in temp*int(rep):
                            stack.append(i)
                else:
                    stack.append(i)
            return ''.join(stack)  