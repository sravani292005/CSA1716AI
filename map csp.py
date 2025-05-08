def is_valid(graph, colors, node, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

# Backtracking function to color the map
def color_map(graph, num_colors, colors, node):
    if node == len(graph):  # All nodes are colored
        return True
    
    for color in range(1, num_colors + 1):
        if is_valid(graph, colors, node, color):
            colors[node] = color
            if color_map(graph, num_colors, colors, node + 1):
                return True
            colors[node] = 0  # Backtrack
            
    return False

# Example Map Graph (Adjacency List)
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

num_colors = 3  # Maximum colors available
colors = [0] * len(graph)  # Assigning 0 initially

if color_map(graph, num_colors, colors, 0):
    print("Solution found:", colors)
else:
    print("No solution found")