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
def astar_search(graph, start, goal, h):
    queue = [(0 + h[start], 0, start, [start])]
    visited = set()  
    while queue:
        f_cost, g_cost, node, path = heapq.heappop(queue)        
        if node not in visited:
            visited.add(node)
            if node == goal:
                return path, g_cost      
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    new_g = g_cost + weight
                    new_f = new_g + h[neighbor]
                    heapq.heappush(queue, (new_f, new_g, neighbor, path + [neighbor]))
    return [], float("inf")
path, cost = astar_search(graph, 'A', 'F', heuristic)
print("A* Path:", path)
print("A* Total Cost:", cost)