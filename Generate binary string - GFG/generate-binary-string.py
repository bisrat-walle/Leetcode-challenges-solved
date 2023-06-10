#User function Template for python3

from collections import deque


class Solution:
    def generate_binary_string(self,s):
        path = []
        ans = []
        def dfs(i):
            if i >= len(s):
                ans.append("".join(path))
                return
            if s[i] == "?":
                path.append("0")
                dfs(i+1)
                path.pop()
                path.append("1")
                dfs(i+1)
                path.pop()
            else:
                path.append(s[i])
                dfs(i+1)
                path.pop()
        
        dfs(0)
        return ans
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		s= input()
		ob = Solution()
		ans = ob.generate_binary_string(s)
		for i in ans:
		    print(i, end = " ")
		print()
# } Driver Code Ends