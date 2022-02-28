class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.di = {}
        self.winners = [None]*len(times)
        for i in self.persons:
            self.di[i] = 0
        temp_win = None
        freq = -1
        for i in range(len(self.times)):
            self.di[self.persons[i]] += 1
            temp_win = self.persons[i] if self.di[self.persons[i]] >= freq else temp_win
            freq = self.di[temp_win]
            self.winners[i] = temp_win
            
            
        
        # print("di", self.di,"Times", times, "winners", self.winners)
        

    def q(self, t: int) -> int:
        pos = self.binary_search(self.times, t, 0, len(self.times))
        
        # print(pos)
        if pos < len(self.times) and self.times[pos] > t:
            pos -= 1
        if pos >= len(self.times):
            pos = len(self.times)-1
        # print(pos, len(self.persons))
        return self.winners[pos]
        
        
    def binary_search(self, arr, val, left, right):
        if left >= right:
            return left
        mid = left + (right-left)//2
        if val == arr[mid]:
                return mid
        if val < arr[mid]:
                return self.binary_search(arr, val, left, mid-1)
        return self.binary_search(arr, val, mid+1, right)
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)