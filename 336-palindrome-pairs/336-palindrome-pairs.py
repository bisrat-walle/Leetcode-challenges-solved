class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        reversed_words = {}
        for index in range(len(words)):
            word = words[index]
            reversed_words[word[::-1]] = index
    
        for index in range(len(words)):
            word = words[index]
            if word != "" and "" in reversed_words:
                if word == word[::-1]: # if palindrome by itself
                    ans.append([index, reversed_words[""]])
                    ans.append([reversed_words[""], index])

            if word in reversed_words and reversed_words[word] != index:
                ans.append([index, reversed_words[word]])
                
            for index2 in range(len(word)):
                
                if word[index2:] in reversed_words:
                    if word[:index2] == word[index2-1::-1]: # if the remaining is palindrome
                        ans.append([reversed_words[word[index2:]], index])
                
                if word[:index2] in reversed_words:
                    if word[index2:] == word[:index2-1:-1]: # if the remaining is palindrome
                        ans.append([index, reversed_words[word[:index2]]])
                    
        return ans