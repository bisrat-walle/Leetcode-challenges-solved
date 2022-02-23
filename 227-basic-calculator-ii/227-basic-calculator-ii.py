class Solution:
    def calculate(self, s: str) -> int:
        s = ''.join([i for i in s if i != " "])
        try:
            return int(s)
        except:
            pass
        
        s = s.strip()
        an = 0
        operations1 = ['/', '*']
        operations2 = ['+', '-']
        stack = []
        n = len(s)
        i = 0
        
         
        while i < n:
            num = ""
            while i < n and ( s[i] not in operations1 and s[i] not in operations2):
                num += s[i]
                i += 1
            stack.append(num.strip())
            if i<n:
                stack.append(s[i])
                i += 1
        mult_div = []
        i = 0
        n = len(stack)
        while i < n:
            # print(stack[i])
            if stack[i] in operations1:
                left = mult_div.pop()
                # print(le)
                if stack[i] == "*":
                    mult_div.append(self.mul(left, stack[i+1]))
                else:
                    mult_div.append(self.div(left, stack[i+1]))
                i += 2
            else:
                mult_div.append(stack[i])
                i += 1
        
        if len(mult_div) == 1:
            return mult_div[0]
        
        # print(mult_div)
        
        an = []
        i = 0
        n = len(mult_div)
        while i < n:
            if mult_div[i] in operations2:
                left = an.pop()
                # print(le)
                if mult_div[i] == "+":
                    # print(mult_div, i)
                    an.append(self.add(left, mult_div[i+1]))
                else:
                    an.append(self.sub(left, mult_div[i+1]))
                i += 2
            else:
                an.append(mult_div[i])
                i += 1 
        
        # print(stack, mult_div, an)
        
        return an[0]
            
    
    
    def add(self, n1, n2):
        # print("add", n1, n2)
        return int(n1)+int(n2)
    
    def sub(self, n1, n2):
        return int(n1)-int(n2)
    
    def mul(self, n1, n2):
        return int(n1)*int(n2)
    
    def div(self, n1, n2):
        return int(int(n1)/int(n2))
            