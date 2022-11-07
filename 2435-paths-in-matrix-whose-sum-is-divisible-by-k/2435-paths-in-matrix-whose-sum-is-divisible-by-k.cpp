class Solution {
public:
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        int n = grid.size(), m = grid[0].size();
        int mod = 1000000007;
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(m, vector<int>(k, 0)));
        
        dp[0][0][grid[0][0]%k] = 1;
        for (int i=0; i < n; i++){
            for (int j=0; j < m; j++){
                for (int l=0; l < k; l++){
                    if (i > 0){
                        int new_mod = (l+grid[i][j])%k;
                        dp[i][j][new_mod] += dp[i-1][j][l]%mod;
                    }
                    if (j > 0){
                        int new_mod = (l+grid[i][j])%k;
                        dp[i][j][new_mod] += dp[i][j-1][l]%mod;
                    }
                }
            }
        }
                   
        return dp[n-1][m-1][0]%mod;
    }
};