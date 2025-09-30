def bfs(tree, root, g):
    result = []
    def level(nodes):
        if len(nodes) == 0:
            return
        n_node = []
        for n in nodes:
            result.append(n)
            if result[-1] == g:
                return 
            for c in tree[n]:
                n_node.append(c)
        level(n_node)
    level([root])
    return result
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}
print("without queue")
print(bfs(tree,'A',"F"))




def bfs(g, start, goal):
    queue = [start]
    v = []
    while queue:
        node = queue.pop(0)  
        v.append(node)
        if node == goal:
            print("Found the goal:", node)
            return v
        for n in g[node]:
            if n not in v and n not in queue:
                queue.append(n)
    return v
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}
result = bfs(graph, 'A', 'E')
print("with queue")
print("Output Nodes", result)
