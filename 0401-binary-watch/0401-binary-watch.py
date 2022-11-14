class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        def rec(turnedOn, current=[0], pos=0):
            if not turnedOn:
                current = current[0]
                hour = 0
                minute = 0
                for i in range(10):
                    if i < 4:
                        hour |= current&(1<<i)
                    else:
                        on = current&(1<<i)
                        i -= 4
                        if on:
                            minute |= (1<<i)
                        
                # print(hour, minute)
                if (not (0 <= hour <= 11)) or (not (0 <= minute <= 59)):
                    return
                    
                minute = str(minute)
                minute = "0"+minute if len(minute) == 1 else minute
                ans.append(f"{hour}:{minute}")
                return
            for i in range(pos, 10):
                if not current[0]&(1<<i):
                    current[0] |= (1<<i)
                    rec(turnedOn-1, current, i)
                    current[0] &= (~(1<<i))
        rec(turnedOn)
        return ans