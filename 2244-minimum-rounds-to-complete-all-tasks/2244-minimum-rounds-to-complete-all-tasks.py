class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        ans = 0
        for value in counter.values():
            if value == 1:
                return -1
            div3 = value//3
            ans += div3
            if value%3 != 0:
                ans += 1
        
        return ans