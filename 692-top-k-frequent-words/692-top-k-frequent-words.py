from heapq import *

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        # word: count pair
        di = {}
        for i in words:
            if i in di.keys():
                di[i] += 1
                continue
            di[i] = 1
        
        # count : word pair
        count = {}
        for i in di.keys():
            if di[i] in count.keys():
                count[di[i]].append(i)
                continue
            count[di[i]] = [i]
        
        # sorting the lists
        for i in count.keys():
            count[i].sort()
        
        # Since I am going to use the built-in python heap, which
        # is originally minheap, I will multiply all numbers -1
        # Inorder to internally consider as maxheap
        
        frequencies = []
        for i in count.keys():
            frequencies.append(-i)
        
        heapify(frequencies)
        print(count,frequencies, di)
        
        an = []
        
        while k > 0:
            largest_freq = -heappop(frequencies)
            lis = count[largest_freq]
            if len(lis) <= k:
                an.extend(lis)
                k -= len(lis)
                continue
            an.extend(lis[:k])
            # return an
            break
        return an        
            
        
        
        