class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        slots = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        def moveUp(s, i):
            l =  list(s)
            l[i] = slots[(slots.index(s[i])+1)%len(slots)]
            return ''.join(l)

        
        def moveDown(s, i):
            l =  list(s)
            l[i] = slots[(slots.index(s[i])-1)%len(slots)]
            return ''.join(l)
        
        dead_set = set(deadends)
        queue = deque([('0000', 0)])
        visited = set('0000')

        while queue:
            (string, steps) = queue.popleft()
            if string == target:
                return steps
            if string in dead_set:
                continue
                
            for i in range(4):
                up = moveUp(string,i)
                if up not in visited:
                    visited.add(up)
                    queue.append((up, steps+1))  
                    
                down = moveDown(string,i)
                if down not in visited:
                    visited.add(down)
                    queue.append((down, steps+1))   

        return -1