class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        ln = len(rooms)
        is_valid = lambda i, j: 0 <= i < ln
        visited = set()
        def dfs(i):
            visited.add(i)
            for neigh in rooms[i]:
                if neigh not in visited:
                    dfs(neigh)
        dfs(0)
        return len(visited) == ln
        