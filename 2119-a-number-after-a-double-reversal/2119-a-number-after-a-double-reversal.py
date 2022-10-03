class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        num_array = list(str(num))
        num_array.reverse()
        while num_array and num_array[0] == "0":
            num_array.pop(0)
        num_array.reverse()
        while num_array and num_array[0] == "0":
            num_array.pop(0)
        return int("".join(num_array)) == num