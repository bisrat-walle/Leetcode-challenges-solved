class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        for index in range(1, len(pref)):
            arr.append(pref[index-1]^pref[index])
        return arr