class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bitArray = [0]*32
        for i in range(32):
            mask = 31-i
            for num in nums:
                if (num>>mask)&1:
                    bitArray[i] += 1
            bitArray[i] = int(bool(bitArray[i]%3))
        pos = True
        if bitArray[0]:
            pos = False
            bitArray = map(lambda k: 0 if k else 1, bitArray)
            
        binaryString = "".join(map(str, bitArray))
        # print(binaryString)
        res = int(binaryString, 2)
        if not pos:  res+= 1
        return res if pos else res*-1
                