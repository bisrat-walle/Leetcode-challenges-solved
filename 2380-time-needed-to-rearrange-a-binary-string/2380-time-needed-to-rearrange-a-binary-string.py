class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans = 0
        while True:
            count = s.count("01")
            if count == 0:
                break
            s = s.replace("01", "10")
            ans += 1
        return ans