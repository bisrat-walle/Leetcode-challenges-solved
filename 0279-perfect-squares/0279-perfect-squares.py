n = 10**4

perfectSquares = []
perfectSquaresSet = set()
for i in range(1, n+1):
    if i**2 <= n:
        perfectSquares.append(i**2)
        perfectSquaresSet.add(i**2)

dp = [float("inf")]*(n+1)
dp[0] = 0
for i in range(1, n+1):
    if i in perfectSquaresSet:
        dp[i] = 1
        continue
    for j in perfectSquares:
        if j > n:
            break
        dp[i] = min(dp[i], dp[i-j]+dp[j])


class Solution:
    def numSquares(self, n: int) -> int:
        return dp[n]
