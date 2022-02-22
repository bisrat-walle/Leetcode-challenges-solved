class Solution:
    def frequencySort(self, s: str) -> str:
        di = {}
        for i in s:
            if i in di.keys():
                di[i] += 1
                continue
            di[i] = 1
        an = ""
        for i in sorted(di.items(), key=lambda k:k[1], reverse=True):
            an += i[0] * i[1]
        
        return an
        