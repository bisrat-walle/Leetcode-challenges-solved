class Solution {
public:
    int hammingWeight(uint32_t n) {
     int ones = 0;
     for (int shift=31; shift>=0; shift--){
         if (n&1<<shift){
             ones += 1;
         }
     }
     return ones;
    }
};