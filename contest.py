from collections import defaultdict, deque
import sys

n = int(input())
input_ = [input() for i in range(n)]

graph = []


for i in range(1, n):
    pre = input_[i-1]
    post = input_[i]
    for i in range(min(len(post), len(pre))):
        if pre[i] == post[i]:
            continue
        if pre[i] < post[i]:
            graph.append([pre[i] , post[i]])
        else:
            graph.append([post[i], pre[i]])
        break

outgoing = defaultdict(set)
inDegree = defaultdict(int)

for pre, post in graph:
    inDegree[post] += 1
    outgoing[pre].add(pre)

queue = deque()

for node in outgoing.keys():
    if inDegree[node] == 0:
        queue.append(node)

if not queue:
    print("Impossible")
    sys.exit(0)
    
an = ""

while queue:
    current_node = queue.popleft()
    an += current_node
    for neigh in outgoing[current_node]:
        inDegree[neigh] -= 1
        if inDegree[neigh] == 0:
            queue.append(neigh)

    

print(an)