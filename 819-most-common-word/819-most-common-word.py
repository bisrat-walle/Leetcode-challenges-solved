class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = []
        temp = ""
        for i in paragraph:
            print(i, temp)
            if i.isalpha():
                temp += i.lower()
            else:
                if temp != "":
                    words.append(temp)
                temp = ""
        if temp != "":
            words.append(temp)
        # print(words)
        banned = set(map(lambda k:k.lower(), banned))
        counter = defaultdict(int)
        for i in words:
            if i not in banned:
                counter[i] += 1
        # print(counter)
        return list(sorted(counter.keys(), key=lambda k:counter[k], reverse=True))[0]