class Solution:
    def sortSentence(self, s: str) -> str:
        wordsnum = s.split()
        dic = {}
        for i in wordsnum:
            dic[int(i[-1])] = i[:-1]
        st = ""
        for i in sorted(dic.keys()):
            st += dic[i] + " "
        return st[:-1]
                            
            
        