class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda a:-a[1])
        # print(boxTypes)
        an, index = 0, 0
        current = truckSize
        while index < len(boxTypes):
            if current == 0:
                break
            dif = min(current, boxTypes[index][0])
            current -= dif
            an += dif*boxTypes[index][1]
            index += 1
        return an
        