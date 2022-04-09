from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        inDegrees = defaultdict(int, {k: 0 for k in recipes})
        outgoing = defaultdict(set)
        supplies = set(supplies)
        
        for i in range(len(recipes)):
            all_supplied = True
            for ingredient in ingredients[i]:
                if ingredient not in supplies:
                    outgoing[ingredient].add(recipes[i])
                    inDegrees[recipes[i]] += 1
                    all_supplied = False
        
        # print(inDegrees, outgoing)
        
        if not outgoing:
            return recipes
        
        queue = deque()
        topological_sort = []
        
        for i in inDegrees.keys():
            if inDegrees[i] == 0:
                queue.append(i)
        while queue:
            current_recipe = queue.popleft()
            topological_sort.append(current_recipe)
            for neigh in outgoing[current_recipe]:
                inDegrees[neigh] -= 1
                if inDegrees[neigh] == 0:
                    queue.append(neigh)
        return topological_sort