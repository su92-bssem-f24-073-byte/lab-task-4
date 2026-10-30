import heapq
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4), ('E', 1)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 4,
    'E': 1,
    'F': 0
}
def greedy_search(graph, start, goal, h):
    queue = [(h[start], start, [start])]
    visited = set()   
    while queue:
        _, node, path = heapq.heappop(queue)      
        if node not in visited:
            visited.add(node)
            if node == goal:
                return path           
            for neighbor, _ in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (h[neighbor], neighbor, path + [neighbor]))
    return []
print("Greedy Search Path:", greedy_search(graph, 'A', 'F', heuristic))