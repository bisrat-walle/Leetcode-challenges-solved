class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.last_cnt = 0
        self.last_num = None

    def consec(self, num: int) -> bool:
        if self.last_num == num:
            self.last_cnt += 1
        else:
            self.last_cnt = 1
            self.last_num = num
        if self.last_cnt >= self.k and num == self.value:
            return True
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)