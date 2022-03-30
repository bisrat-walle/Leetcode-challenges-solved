class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()
        last_occurrence = {}
        n = len(s)
        for i in range(n):
            last_occurrence[s[i]] = i

        for i in range(n):
            
            if s[i] in visited:
                continue
                
            while stack and stack[-1] > s[i] and last_occurrence[stack[-1]] > i:
                visited.remove(stack.pop())
            
            
            visited.add(s[i])
            
            stack.append(s[i])

        return ''.join(stack)
    