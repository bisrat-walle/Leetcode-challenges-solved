from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        original_count = Counter(words)
        word_size = len(words[0])
        n = len(words)
        left, right = 0, 1
        ans = []
        for index in range(len(s)):
            temp_index = index
            current_count = defaultdict(int)
            current_str = s[temp_index:temp_index+word_size]
            found_counter = 0
            while current_str in original_count:
                if found_counter == n:
                    break
                current_count[current_str] += 1
                if current_count[current_str] > original_count[current_str]:
                    break
                found_counter += 1
                temp_index += word_size
                current_str = s[temp_index:temp_index+word_size]
            if found_counter == n:
                ans.append(index)
        return ans
                
            
                
            