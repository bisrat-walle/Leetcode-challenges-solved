from collections import deque

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = deque(digits)
        carry = 0
        an = []
        for index in reversed(range(len(digits))):
            if index == len(digits)-1:
                current = str(digits[index]+1)
                digits[index] = int(current[-1])
                carry = int(current[:-1]) if len(current) > 1 else 0
            else:
                current = str(digits[index]+carry)
                digits[index] = int(current[-1])
                carry = int(current[:-1]) if len(current) > 1 else 0
        if carry != 0:
            carry = list(reversed(list(map(int, list(str(carry))))))
            for dig in carry:
                digits.appendleft(dig)
        
        return digits
                