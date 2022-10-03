class Solution:
    def reverseBits(self, n: int) -> int:
        bitArray = list(bin(n)[2:])
        bitArray = ["0"]*(32-len(bitArray))+bitArray
        i, j = 0, len(bitArray)-1
        while i < j:
            bitArray[i], bitArray[j] = bitArray[j], bitArray[i]
            i += 1
            j -= 1
        return int("".join(bitArray), 2)