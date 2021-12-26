class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0]*n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i-1]+nums[i]
        dequeue = []
        an = -1
        for i in range(n):
            if pre[i] >= k:
                if an == -1:
                    an = i + 1
                else:
                    an = min(an, i+1)
            ysum = pre[i]
            xsum = ysum - k
            while dequeue and pre[dequeue[0]] <= xsum:
                if an == -1:
                    an = i - dequeue.pop(0)
                else:
                    an = min(an, i - dequeue.pop(0))
            while dequeue and pre[dequeue[-1]] >= pre[i]:
                dequeue.pop()
            dequeue.append(i)
        return an
            
                    