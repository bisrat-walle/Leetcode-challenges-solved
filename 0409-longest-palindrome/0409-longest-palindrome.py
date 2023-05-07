class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        zipped = []
        for key in counter:
            zipped.append((counter[key], key))
            
        extras = 0
        ans = 0
        for cnt, key in zipped:
            current = 2 * (cnt//2)
            ans += current
            extras += cnt - current
            
        if extras:
            ans += 1
        return ans