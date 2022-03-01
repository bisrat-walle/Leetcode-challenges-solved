class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0]*len(isConnected)
        provinces = 0
        for i in range(len(isConnected)):
            if (visited[i] == 0):
                provinces += 1;
                self.dfs(isConnected, visited, i);
                
        return provinces;
    
    
    def dfs(self, isConnected, visited, i):
         for j in range(len(isConnected)):
            if (isConnected[i][j] == 1 and visited[j] == 0):
                visited[j] = 1
                self.dfs(isConnected, visited, j)