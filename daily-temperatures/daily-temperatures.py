class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        an = [0] * n
        for i in reversed(range(n)):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                an[i] = stack[-1] - i
            stack.append(i)
        return an
                        