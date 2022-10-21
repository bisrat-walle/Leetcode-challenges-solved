class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int> dp;
        for(int i=0; i < nums.size(); i++){
            dp.push_back(214748364);
        }
        dp[dp.size()-1] = 0;
            
        for(int i=nums.size()-2; i > -1 ; i--){
            for(int j=1; j <= nums[i] ; j++){
                if (i+j >= nums.size()){
                    break;
                }
                dp[i] = min(dp[i], 1+dp[i+j]);
            }
        }
        return dp[0];
    }
};