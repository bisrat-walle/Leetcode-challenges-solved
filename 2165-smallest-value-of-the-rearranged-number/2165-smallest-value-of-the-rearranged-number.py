class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        l = list(map(int, list(str(abs(num)))))
        if num < 0:
            l.sort(reverse=True)
        else:
            l.sort()
        i = 0
        while i < len(l) and l[i] == 0:
            i += 1
        
        l[i], l[0] = l[0], l[i]
        
        an = int("".join(map(str, l)))
        if num < 0:
            return -1 * an
        return an
        
        