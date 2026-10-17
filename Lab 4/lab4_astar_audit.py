import heapq

def astar(graph, h, start, goal):

    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    expanded_nodes = []

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            return g, path, expanded_nodes

        if g > best.get(node, float("inf")):
            continue

        expanded_nodes.append(node)

        for nxt, weight in graph.get(node, []):
            ng = g + weight
            if ng < best.get(nxt, float("inf")):
                best[nxt] = ng
                heapq.heappush(pq, (ng + h[nxt], ng, nxt, path + [nxt]))

    return float("inf"), [], expanded_nodes

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

h_admissible = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}

h_ucs = {"S": 0, "A": 0, "B": 0, "C": 0, "G": 0}

h_overestimate = {"S": 5, "A": 4, "B": 4, "C": 10, "G": 0}

if __name__ == "__main__":
    print("=== 1. Standard A* Search ===")
    cost, path, expanded = astar(graph, h_admissible, "S", "G")
    print(f"Path: {path} | Cost: {cost} | Expanded Nodes: {expanded}")

    print("\n=== 2. UCS Control Run (h = 0) ===")
    cost_ucs, path_ucs, expanded_ucs = astar(graph, h_ucs, "S", "G")
    print(f"Path: {path_ucs} | Cost: {cost_ucs} | Expanded Nodes: {expanded_ucs}")

    print("\n=== 3. A* with Overestimated Heuristic (h(C) = 10) ===")
    cost_over, path_over, expanded_over = astar(graph, h_overestimate, "S", "G")
    print(f"Path: {path_over} | Cost: {cost_over} | Expanded Nodes: {expanded_over}")