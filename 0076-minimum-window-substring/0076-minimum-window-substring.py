class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        counter = Counter(t)
        valid = 0
        left = 0
        global_left = global_right = -1
        current_mx = float("inf")
        runningCounter = defaultdict(int)
        for right in range(n):
            runningCounter[s[right]] += 1
            if s[right] in counter and runningCounter[s[right]] == counter[s[right]]:
                valid += counter[s[right]]
            
            while left<n and (s[left] not in counter or \
                    runningCounter[s[left]] > counter[s[left]]):
                runningCounter[s[left]] -= 1
                left += 1
            
            if valid == len(t):
                if right-left+1 < current_mx:
                    current_mx = right-left+1
                    global_left = left
                    global_right = right
        return s[global_left:global_right+1] if global_left != -1 else ""