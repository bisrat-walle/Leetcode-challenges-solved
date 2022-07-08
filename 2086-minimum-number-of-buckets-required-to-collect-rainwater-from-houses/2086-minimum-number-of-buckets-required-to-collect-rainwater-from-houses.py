class Solution:
    def minimumBuckets(self, street: str) -> int:
        n = len(street)
        buckets = 0
        prevBucket = -2
        for i, c in enumerate(street):
            if c == '.' or prevBucket == i - 1:
                continue
            
            buckets += 1
            if i != n - 1 and street[i + 1] == '.':
                prevBucket = i + 1
            elif not i or street[i - 1] == 'H':
                return -1
        
        return buckets