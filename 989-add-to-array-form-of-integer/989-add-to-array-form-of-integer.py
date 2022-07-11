class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num[-1] += k
        for i in range(len(num) - 1, -1, -1):
            carry, num[i] = divmod(num[i], 10)
            if i: 
                num[i-1] += carry
        if carry:
            num = list(map(int, str(carry))) + num
        return num