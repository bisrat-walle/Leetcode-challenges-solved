class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def addDigits(a, b, carry):
            if a == b == "1":
                if carry == 0:
                    return 0, 1
                return 1, 1
            if a == b == "0":
                if carry == 0:
                    return 0, 0
                return 1, 0
            if carry == 0:
                return 1, 0
            return 0, 1
        a = deque(list(a))
        b = deque(list(b))
        mx = max(len(a), len(b))
        for _ in range(len(a), mx):
            a.appendleft("0")
        for _ in range(len(b), mx):
            b.appendleft("0")
            
        res = deque()
        carry = 0
        for index in reversed(range(mx)):
            current_res, carry = addDigits(a[index], b[index], carry)
            res.appendleft(str(current_res))
        
        if carry:
            res.appendleft(str(carry))
        
        # print(res)
        return "".join(res)
        