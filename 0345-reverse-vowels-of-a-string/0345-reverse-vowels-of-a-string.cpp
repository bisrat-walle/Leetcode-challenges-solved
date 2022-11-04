class Solution {
public:
    string reverseVowels(string s) {
        set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        vector<int> indexes;
        for (int i=0; i < s.length(); i++){
            if (vowels.count(s[i])) {
                indexes.push_back(i);
            }
        }
        
        
        int left = 0, right = indexes.size()-1;
        while (left < right){
            char temp = s[indexes[left]];
            s[indexes[left]] = s[indexes[right]];
            s[indexes[right]] = temp;
            left++;
            right--;
        }
        
        return s;
    }
};