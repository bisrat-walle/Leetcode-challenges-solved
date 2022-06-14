class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def get_key(word):
            letters = list(word)
            letters.sort()
            return "".join(letters)

        key = get_key(words[0])
        an = [words[0]]

        for i in range(1, len(words)):
            new_key = get_key(words[i])
            if new_key != key :
                key = new_key
                an.append(words[i])

        return an