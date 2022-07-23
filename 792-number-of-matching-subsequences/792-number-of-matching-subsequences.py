class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.word_end_count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, count) -> None:
        current = self.root
        for letter in word:
            if letter not in current.nodes:
                current.nodes[letter] = TrieNode()
            current = current.nodes[letter]
        current.word_end_count = count

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        counter = Counter(words)
        self.matching_subsequence = 0  
        trie = Trie()
        for word in words:
            trie.insert(word, counter[word])
        def count_matching(node, i=-1):
            for child in node.nodes:
                pos = s.find(child, i+1, len(s))
                if pos != -1:
                    self.matching_subsequence += node.nodes[child].word_end_count
                    count_matching(node.nodes[child], pos)
                    
        count_matching(trie.root)
        return self.matching_subsequence