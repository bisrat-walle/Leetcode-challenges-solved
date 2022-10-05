class Solution {
public:
    string longestPalindrome(string s) {
        int ansLeft=0, ansRight=0;
        int mx = 0;
        int n = s.length();
        for (int index=0; index < n; index++) {
            int left = index, right = index;
            while (left > 0 && right < n-1 && s[left-1] == s[right+1]) {
                left--;
                right++;
            }
            int currentSize = right-left+1;
            if (currentSize > mx){
                mx = currentSize;
                ansLeft = left;
                ansRight = right;
            }
            
            if (index == n-1 || s[index] != s[index+1]){
                continue;
            }
            
            left = index;
            right = index+1;
            while (left > 0 && right < n-1 && s[left-1] == s[right+1]) {
                left--;
                right++;
            }
            currentSize = right-left+1;
            if (currentSize > mx){
                mx = currentSize;
                ansLeft = left;
                ansRight = right;
            }
        }
        return s.substr(ansLeft, mx);
    }
};