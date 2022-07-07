# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

import random

class Solution:
    def findSecretWord(self, wordList: List[str], master: 'Master') -> None:
        candidates = []
        numguesses = 10
        for _ in range(numguesses):
            current_word = random.choice(wordList)
            guess_result = master.guess(current_word)
            newWordList = []
            for word in wordList:
                matched = 0
                for index in range(len(word)):
                    if word[index] == current_word[index]:
                        matched += 1
                if matched == guess_result:
                    newWordList.append(word)
            wordList = newWordList