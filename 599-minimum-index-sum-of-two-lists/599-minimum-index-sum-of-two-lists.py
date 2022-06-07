class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index1 = {}
        index2 = {}
        for i, j in enumerate(list1):
            index1[j] = i
        for i, j in enumerate(list2):
            index2[j] = i
        
        set1 = set(list1)
        inter = {}
        for i in list2:
            if i in set1:
                inter[i] = index1[i] + index2[i]
            
        sorted_items = sorted(inter.items(), key=lambda k:k[1])
        an = []
        for i in sorted_items:
            if i[1] == sorted_items[0][1]:
                an.append(i[0])
        
        return an
            