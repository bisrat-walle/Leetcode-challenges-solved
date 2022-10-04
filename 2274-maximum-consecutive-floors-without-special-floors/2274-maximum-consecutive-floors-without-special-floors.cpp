class Solution {
public:
    int maxConsecutive(int bottom, int top, vector<int>& special) {
        int n = special.size();
        int mx = 0, count = 0;
        sort(special.begin(),special.end());
        if(top > special[n-1])
            mx= max(mx,(top - special[n-1]));

        if(bottom < special[0])
            mx = max(mx,(special[0] - bottom));

        for(int i = 1; i < n; i++){
            if(special[i] - special[i-1] > 1)
                mx = max(mx, (special[i]-special[i-1])-1);
        }
        return mx;
    }
};