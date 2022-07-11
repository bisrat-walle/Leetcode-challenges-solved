class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mult = []
        max_ln = 0
        for index in range(len(num1)-1, -1, -1):
            current = deque([])
            carry = 0
            mu = int(num1[index])
            for index2 in range(len(num2)-1, -1, -1):
                product = str(int(num2[index2])*mu+carry)
                if index2 == 0:
                    current.appendleft(int(product))
                else:
                    current.appendleft(int(product[-1]))
                
                carry = int(product[:-1]) if len(product) > 1 else 0
            for _ in range((len(num1)-index-1)): # padding with 0 to the right
                current.append(0)
            mult.append(current)
            
            max_ln = max(max_ln, len(current))
        
        # padding with 0 to the left
        for current in mult:
            for _ in range(max_ln - len(current)):
                current.appendleft(0)
        # print(mult)
        an = deque([])
        carry = 0
        for i in reversed(range(len(mult[0]))):
            vertial_sum = carry
            for j in reversed(range(len(mult))):
                vertial_sum += mult[j][i]
            temp = str(vertial_sum)
            if i == 0:
                an.appendleft(temp)
            else:
                an.appendleft(temp[-1])
            carry = int(temp[:-1]) if len(temp) > 1 else 0
            # print(vertial_sum, carry, an)
        
        if an[0] == "0":
            return "0"
        return "".join(an)
                
                
            