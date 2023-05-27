
def graph_coloring(graph, num_colors):
    # Create a list to store the color assigned to each vertex
    colors = [0] * len(graph)

    def is_safe(vertex, color):
        # Check if it is safe to color the vertex with the given color
        for neighbor in graph[vertex]:
            if colors[neighbor] == color:
                return False
        return True

    def backtrack(vertex):
        # Base case: All vertices have been assigned colors
        if vertex == len(graph):
            return True

        # Try all possible colors for the current vertex
        for color in range(1, num_colors + 1):
            if is_safe(vertex, color):
                # Assign the color to the vertex
                colors[vertex] = color

                # Recursively backtrack to assign colors to the remaining vertices
                if backtrack(vertex + 1):
                    return True

                # If the current configuration doesn't lead to a solution, backtrack
                colors[vertex] = 0

        return False

    # Start with the first vertex (vertex index 0)
    if backtrack(0):
        # If a solution is found, print the color assignment
        print("Color assignment:")
        for vertex, color in enumerate(colors):
            print(f"Vertex {vertex}: Color {color}")
    else:
        print("No solution found.")

# Gather the graph information from the user
num_vertices = int(input("Enter the number of vertices: "))

graph = {}
for vertex in range(num_vertices):
    neighbors = input(f"Enter the neighbors of vertex {vertex} (separated by spaces): ").split()
    graph[vertex] = [int(neighbor) for neighbor in neighbors]

# Prompt the user to enter the number of colors
num_colors = int(input("Enter the number of colors: "))

# Call the graph_coloring function
graph_coloring(graph, num_colors)