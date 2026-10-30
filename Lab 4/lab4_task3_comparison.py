import heapq
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4), ('E', 1)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}
h1 = {'A': 6, 'B': 4, 'C': 2, 'D': 4, 'E': 1, 'F': 0}
def run_comparison(graph, start, goal, heuristic):
    queue = [(0 + heuristic[start], 0, start, [start])]
    visited = set()  
    while queue:
        f, g, node, path = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == goal:
                return path, g
            for nbr, w in graph.get(node, []):
                if nbr not in visited:
                    ng = g + w
                    nf = ng + heuristic[nbr]
                    heapq.heappush(queue, (nf, ng, nbr, path + [nbr]))
    return [], 0
path, cost = run_comparison(graph, 'A', 'F', h1)
print("Comparison Test Path:", path)
print("Comparison Test Cost:", cost)