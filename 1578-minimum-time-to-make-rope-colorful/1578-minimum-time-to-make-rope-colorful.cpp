#include <algorithm>

class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int left = 0, right = 1;
        int ans = 0;
        
        while (right < neededTime.size()){
            int sum = neededTime[left];
            int mx = neededTime[left];
            while (right < neededTime.size() && colors[left] == colors[right]){
                sum += neededTime[right];
                mx = max(mx, neededTime[right]);
                right += 1;
                
            }
            
            if (mx != sum){
                ans += sum-mx;
            }
            
            left = right;
            right += 1;
        }
        return ans;
    }
};