class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        digits = deque(digits)
        index = len(digits)-1
        while index > -2:
            if index == -1:
                if carry:
                    digits.appendleft(carry)
                break
            new_sum = str(digits[index]+carry)
            digits[index] = int(new_sum[-1])
            if len(new_sum) == 1:
                carry = 0
            else:
                carry = int(new_sum[0])
            index -= 1
        return digits