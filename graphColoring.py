def is_safe(graph, color, node, c):
    """Check if it's safe to assign color c to the node."""
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True

def graph_coloring(graph, m, color, node):
    """Try to color the graph using backtracking."""
    if node == len(graph):  
        return True
    
    for c in range(1, m + 1):
        if is_safe(graph, color, node, c):
            color[node] = c
            if graph_coloring(graph, m, color, node + 1):
                return True
            color[node] = 0  # Backtrack

    return False

# Input: number of vertices and edges
vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

# Create the graph as an    adjacency list
graph = [[] for _ in range(vertices)]

print("Enter the edges (pairs of vertices, e.g., '0 1'):")
for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Input: number of colors
m = int(input("Enter number of colors: "))

# Initialize color array
color = [-1] * vertices

# Solve the graph coloring problem
if graph_coloring(graph, m, color, 0):
    print("Coloring Solution:", color)
else:
    print("No solution")