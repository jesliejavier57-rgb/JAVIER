
# ASSESSMENT 3.3: NON-LINEAR DATA STRUCTURE
# GRAPH USING LAST NAME: JAVIER

# Creating Graph
graph = {
    "J": ["A", "V"],
    "A": ["J", "I", "E"],
    "V": ["J", "R", "E"],
    "I": ["A", "R"],
    "E": ["A", "V"],
    "R": ["I", "V"]
}


# Breadth-First Search (BFS)
def BFS(graph, start):
    visited = [start]
    queue = [start]

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


# Depth-First Search (DFS)
def DFS(graph, node, visited=None):
    if visited is None:
        visited = []

    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for neighbor in graph[node]:
            DFS(graph, neighbor, visited)


# Display Results
print("================================")
print("          GRAPH - JAVIER")
print("================================")

print("\nBFS Traversal:")
BFS(graph, "J")

print("\n\nDFS Traversal:")
DFS(graph, "J")

print("\n================================")
