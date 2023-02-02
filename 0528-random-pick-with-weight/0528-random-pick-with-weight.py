class Solution:

    def __init__(self, w: List[int]):
        self.arr = [i for i in range(len(w))]
        self.prob = []
        total = sum(w)
        for num in w:
            self.prob.append(num/total)

    def pickIndex(self) -> int:
        return random.choices(self.arr, self.prob)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()