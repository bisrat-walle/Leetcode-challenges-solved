class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        res = self.countAndSay(n-1)
        ans = []
        cnt = 1
        for index in range(1, len(res)+1):
            if index == len(res) or res[index] != res[index-1]:
                ans.extend([cnt, res[index-1]])
                cnt = 1
            else:
                cnt += 1
        return "".join(map(str, ans))