class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        stack = []
        ind = 0
        while(ind < len(num)):
            
            if k <= 0:
                break
            curr = num[ind]
            if ind > 0 and stack[-1]>curr:
                while(stack and stack[-1] > curr and k>0):
                    stack.pop()
                    k-=1
            
            stack.append(curr)
            ind += 1
        
        for i in range(ind , len(num)):
            stack.append(num[i])
        
        if k > 0:
            stack = stack[:-k]
        
        s = "".join(stack)
        
        return str(int(s))