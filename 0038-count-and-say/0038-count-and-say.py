class Solution:
    def countAndSay(self, n: int) -> str:
        # Iterative Version 
        current = "1"
        for i in range(1, n):
            res = current
            ans = []
            cnt = 1
            for index in range(1, len(res)+1):
                if index == len(res) or res[index] != res[index-1]:
                    ans.extend([cnt, res[index-1]])
                    cnt = 1
                else:
                    cnt += 1
            current = "".join(map(str, ans))
        return current