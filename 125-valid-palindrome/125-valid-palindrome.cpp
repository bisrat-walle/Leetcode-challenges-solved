#include <string>

class Solution {
public:
    bool isPalindrome(string s) {
        
        string st = "";
        for (int i = 0; i < s.length(); i++){
            if (isalnum(s[i]) && s[i] != ' '){
                st += tolower(s[i]);
            }
        }
        
        cout << st;
        
        int i = 0, j = st.length()-1;
        while (i < j){
            if (st[i] != st[j]){
                return false;
            }
            i += 1;
            j -= 1;
        }
        return true;
    }
};