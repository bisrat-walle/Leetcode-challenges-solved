class Solution {
public:
    bool isIdealPermutation(vector<int>& nums) {
        unsigned long long local_inversions = 0, global_inversions = 0;
        for (int index=0; index<nums.size(); index++){
            
            if (index < nums.size()-1 && nums[index] > nums[index+1]){
                local_inversions++;
            }
                
            // MATH
            if (nums[index] > index) {
                global_inversions += nums[index]-index;
            }
            else if (nums[index] < index){
                global_inversions += index-nums[index]-1;
            }
        }
        
        return global_inversions == local_inversions;
    }
};