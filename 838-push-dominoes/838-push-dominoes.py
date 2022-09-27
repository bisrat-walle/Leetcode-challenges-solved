class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes_list = list(dominoes)
        queue = deque()
        for index in range(len(dominoes)):
            domino = dominoes[index]
            if domino != ".":
                queue.append((index, domino))
        
        while queue:
            left, right = set(), set()
            for _ in range(len(queue)):
                domino = queue.popleft()
                # print(domino)
                if domino[1] == "L" and domino[0] > 0 and dominoes_list[domino[0]-1] == ".":
                    left.add(domino[0]-1)
                if domino[1] == "R" and domino[0] < len(dominoes)-1 and \
                            dominoes_list[domino[0]+1] == ".":
                    right.add(domino[0]+1)
            intersection = left.intersection(right)
            union = left.union(right)
            for index in union:
                if index in intersection:
                    dominoes_list[index] = "."
                elif index in left:
                    dominoes_list[index] = "L"
                    queue.append((index, "L"))
                else:
                    dominoes_list[index] = "R"
                    queue.append((index, "R"))
        return "".join(dominoes_list)
