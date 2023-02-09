class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(map(int, list(str(num))))
        for i in range(len(num)-1):
            mx = i
            for j in range(i+1, len(num)):
                if num[j] >= num[mx]:
                    mx = j
            if i != mx and num[i] != num[mx]:
                num[i], num[mx] = num[mx], num[i]
                break
        
        return int("".join(map(str, num)))
            