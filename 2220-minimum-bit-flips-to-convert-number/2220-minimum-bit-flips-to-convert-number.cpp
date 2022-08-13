class Solution {
public:
    int minBitFlips(int start, int goal) {
        int ans = 0;
        for (int i=30; i >= 0; i--){
            int num1 = start&(1<<i), num2 = goal&(1<<i);
            // cout<<num1<<" "<<num2<<endl;
            if (num1 != num2){
                ans++;
            }
        }
        return ans;
    }
};