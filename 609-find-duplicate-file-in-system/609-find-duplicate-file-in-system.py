from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mapping=defaultdict(list)
        for path in paths:
            tokenized=path.split(" ")
            for index in range(1,len(tokenized)):
                opening_index=tokenized[index].index("(")
                mapping[tokenized[index][opening_index:]].append(\
                    tokenized[0]+"/"+tokenized[index][:opening_index])
        return [p for p in mapping.values() if len(p) > 1]