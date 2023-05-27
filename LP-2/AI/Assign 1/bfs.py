def bfs_recursive(graph, queue, visited):
    if not queue:
        return
    
    current_node = queue.pop(0)
    print(current_node)  # Perform any desired operation on the current node
    
    visited.add(current_node)
    
    for neighbor in graph[current_node]:
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)
    
    bfs_recursive(graph, queue, visited)


# Get user input for the graph
graph = {}
num_nodes = int(input("Enter the number of nodes: "))

for i in range(num_nodes):
    node = input(f"Enter node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (comma-separated): ").split(",")
    graph[node] = neighbors

start_node = input("Enter the starting node: ")

# Perform BFS traversal
bfs_recursive(graph, [start_node], set())