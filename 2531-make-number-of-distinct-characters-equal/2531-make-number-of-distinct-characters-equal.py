class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        
        def insert_and_remove(counter, ch_ins, ch_rm):
            if ch_ins not in counter:
                counter[ch_ins] = 1
            else:
                counter[ch_ins] += 1
            counter[ch_rm] -= 1
            if counter[ch_rm] == 0:
                del counter[ch_rm]
        
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        if len(counter1) > len(counter2):
            counter1, counter2 = counter2, counter1
        n, m = len(counter1), len(counter2)
        for o1 in range(ord('a'), ord('z')+ 1):
            for o2 in range(ord('a'), ord('z')+ 1):
                ch1, ch2 = chr(o1), chr(o2)
                if ch1 not in counter1 or ch2 not in counter2:
                    continue
                insert_and_remove(counter1, ch2, ch1)
                insert_and_remove(counter2, ch1, ch2)
                if len(counter1) == len(counter2):
                    return True
                insert_and_remove(counter1, ch1, ch2)
                insert_and_remove(counter2, ch2, ch1)
        return False
                    
                                     
                                     