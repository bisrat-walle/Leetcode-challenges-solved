class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = deque(list(num1))
        num2 = deque(list(num2))
        an = deque()
        add = []
        for _ in range(len(num1), max(len(num1), len(num2))):
            num1.appendleft("0")
        for _ in range(len(num2), max(len(num1), len(num2))):
            num2.appendleft("0")
        # print(num1, num2)
        carry = 0
        for index in reversed(range(len(num1))):
            current = str(int(num1[index])+int(num2[index]) + carry)
            an.appendleft(current[-1])
            carry = int(current[:-1]) if len(current) > 1 else 0
            # print(int(num1[index]), int(num2[index]), carry)
        
        if carry != 0:
            for digit in reversed(list(str(carry))):
                an.appendleft(digit)
        if an and an[0] == "0":
            return "0"
        return "".join(an)
        