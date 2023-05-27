def dfs_recursive(graph, current_node, visited):
    visited.add(current_node)
    print(current_node)  # Perform any desired operation on the current node
    
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


# Get user input for the graph
graph = {}
num_nodes = int(input("Enter the number of nodes: "))

for i in range(num_nodes):
    node = input(f"Enter node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (comma-separated): ").split(",")
    graph[node] = neighbors

start_node = input("Enter the starting node: ")

# Perform DFS traversal
dfs_recursive(graph, start_node, set())