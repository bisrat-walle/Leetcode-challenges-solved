class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and price >= self.stack[-1][0]:
            val, new_ans = self.stack.pop()
            ans += new_ans
        
        self.stack.append((price, ans))
        
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)