class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        ans = 0
        current = len(arr)
        sorted_ocurr = sorted(counter.values(), reverse=True)
        # print(sorted_ocurr)
        for i in sorted_ocurr:
            if current <= len(arr)//2:
                break
            ans += 1
            current -= i
        return ans