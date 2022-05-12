class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = [int(i) for i in version1.split(".")]
        version2_list = [int(i) for i in version2.split(".")]
        
        min_ln = min(len(version1_list), len(version2_list))
        max_ln = max(len(version1_list), len(version2_list))
        for _ in range(len(version1_list), max_ln):
            version1_list.append(0)
        for _ in range(len(version2_list), max_ln):
            version2_list.append(0)
        
        # print(version1_list, version2_list)
            
        index = 0
        while index < max_ln:
            if version1_list[index] > version2_list[index]:
                return 1
            if version2_list[index] > version1_list[index]:
                return -1
            index += 1
        return 0
        