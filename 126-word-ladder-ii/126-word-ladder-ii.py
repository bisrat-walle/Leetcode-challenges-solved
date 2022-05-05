class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
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
        
        
        visited = set()
        queue = deque([(beginWord, [beginWord])])
        done = False
        an = []
        finished = False
        while queue:
            for _ in range(len(queue)):
                current, seq = queue.popleft()
                if current == endWord:
                    if an and len(an[-1]) < len(seq):
                        finished = True
                        break
                    an.append(seq)
                visited.add(current)
                for j  in di[current]:
                    if j not in visited:
                        queue.append((j, seq+[j]))
            
            if finished:
                break
                    
                       
        return an
    