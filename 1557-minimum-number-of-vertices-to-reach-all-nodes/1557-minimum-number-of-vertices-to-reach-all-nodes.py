class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(int)
        for i in range(n):
            graph[i] == 0
        for i, j in edges:
            graph[j] += 1
        an = []
        for i in range(n):
            if graph[i] == 0:
                an.append(i)
        return an