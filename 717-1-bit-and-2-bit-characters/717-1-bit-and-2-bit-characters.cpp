class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        int i = 0;
        bool lastIsOneBit = false;
        while (i < bits.size()){
            if (bits[i] == 1){
                i += 2;
                lastIsOneBit = false;
            }
            else{
                i++;
                lastIsOneBit = true;
            }
        }
        return lastIsOneBit;
        
    }
};