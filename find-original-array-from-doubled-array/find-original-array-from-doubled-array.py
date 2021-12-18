class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n%2 != 0:
            return []
        changed.sort()
        an = []
        counter = {}
        for i in changed:
            if i in counter.keys():
                counter[i] += 1
            else:
                counter[i] = 1
        for i in changed:
            if i == 0:
                if counter[i] >= 2:
                    counter[i] -= 2
                    an.append(i)
            elif counter[i] !=  0:
                if (2*i) in counter.keys():
                    if counter[2*i] != 0:
                        counter[i] -= 1
                        counter[2*i] -= 1
                        an.append(i)
        if len(an) == n//2:
            return an
        return []
            
                    