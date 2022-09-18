class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = 0
        ans = 0
        for ch in s:
            if ch == "(":
                left += 1
            if ch == ")":
                right += 1
            if left == right:
                ans = max(ans, 2*left)
            if right > left:
                left = right = 0
        
        left = right = 0
        for index in reversed(range(len(s))):
            ch = s[index]
            if ch == "(":
                left += 1
            if ch == ")":
                right += 1
            if left == right:
                ans = max(ans, 2*left)
            if left > right:
                left = right = 0
        return ans