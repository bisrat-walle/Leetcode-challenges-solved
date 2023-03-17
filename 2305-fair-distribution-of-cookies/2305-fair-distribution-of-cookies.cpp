class Solution {
public:
    int ans = 8000000;
    int k1;
    vector<int> arr, ass;
    
    void backtrack(int index){
        if (index >= arr.size()){
            ans = min(ans, *max_element(ass.begin(), ass.end()));
            return;
        }
            

        if (ans <= *max_element(ass.begin(), ass.end()))
            return;

        for(int i=0; i < k1; i++){
            ass[i] += arr[index];
            backtrack(index+1);
            ass[i] -= arr[index];
        }
    }

    
    int distributeCookies(vector<int>& cookies, int k) {
        k1 = k;
        arr = cookies;
        sort(arr.rbegin(), arr.rend());
        ass.resize(k, 0);
        backtrack(0);
        
        return ans;
    }
};