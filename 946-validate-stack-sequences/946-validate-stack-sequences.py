class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped_index = 0
        pushed_index = 0
        temp = []
        while popped:
            if temp and popped[0] == temp[-1]:
                temp.pop()
                popped.pop(0)
                
            else:
                if pushed_index < len(pushed):
                    temp.append(pushed[pushed_index])
                    pushed_index += 1
                else:
                    return False
        if popped:
            return False
        return True