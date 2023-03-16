class Solution {
public:
    int ans = 8000000;
    int k1;
    vector<int> arr;
    vector<int> ass;
    
    int getMax(){
        int mx = -1;
        for(int i=0; i < ass.size(); i++){
            if (mx < ass[i]){
                mx = ass[i];
            }
        }
        return mx;
    }
    
    void backtrack(int index){
        if (index >= arr.size()){
            ans = min(ans, getMax());
            return;
        }
            

        if (ans <= getMax())
            return;

        for(int i=0; i < k1; i++){
            ass[i] += arr[index];
            backtrack(index+1);
            ass[i] -= arr[index];
        }
    }

    
    int distributeCookies(vector<int>& cookies, int k) {
        k1 = k;
        for(int i=0; i < cookies.size(); i++){
            arr.push_back(cookies[i]);
        }
        for(int i=0; i < k; i++){
            ass.push_back(0);
        }
        
        backtrack(0);
        
        return ans;
        return 0;
    }
};