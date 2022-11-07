class Solution {
public:
    int maximum69Number (int num) {
        string num_str = to_string(num);
        bool changed = false;
        for (int i=0; i<num_str.size(); i++){
            if (num_str[i] == '6' && !changed){
                num_str[i] = '9';
                changed = true;
            }
        }
        
        return stoi(num_str);
    }
};