class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        def getAllDiffByOne(word):
            an = []
            # Only 260 Possiblities
            for i in range(len(word)):
                for j in range(97, 123):
                    key = list(word)
                    key[i] = chr(j)
                    new_key = "".join(key)
                    if new_key in word_set:
                        an.append(new_key)
            return an
        
        di = {}
        di[beginWord] = getAllDiffByOne(beginWord)
        for i in wordList:
            di[i] = getAllDiffByOne(i)
        
        
        
        an = 1
        visited = set()
        queue = [beginWord]
        while queue:
            
            for i in queue:
                if i == endWord:
                    return an
                visited.add(i)
            an += 1
            temp = []
            for i in queue:
                for j in di[i]:
                    if j not in visited:
                        temp.append(j)
                di[i] = []
            queue = temp
        return 0
    