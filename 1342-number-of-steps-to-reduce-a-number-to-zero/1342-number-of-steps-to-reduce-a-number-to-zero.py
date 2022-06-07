class Solution:
    def numberOfSteps(self, num: int) -> int:
        an = 0
        while num > 0:
            if num&1 == 0:
                num = num>>1
            else:
                num = num>>1
                num = num<<1
            an += 1
        return an