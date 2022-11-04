class Solution {
public:
    int countPrimes(int n) {
        if (n <= 2){
            return 0;
        }
        
        vector<bool> isPrime(n+1, true);
        int ans = 0;
        for (int i=2; i < n; i++){
            if (isPrime[i]) {
                for (long j=(long) i* (long) i; j<(long) n; j+=(long) i){
                    isPrime[j] = false;
                }
                ans += 1;
            }
            // for (int k=0; k <= n; k++){
            //     cout << isPrime[k] << " ";
            // }
            // cout << endl;
        }
        
        
        return ans;
    }
};