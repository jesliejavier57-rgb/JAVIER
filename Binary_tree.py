
# ASSESSMENT 3.3 - BINARY TREE
# LAST NAME: JAVIER

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree
root = Node("J")
root.left = Node("A")
root.right = Node("V")
root.left.left = Node("I")
root.left.right = Node("E")
root.right.right = Node("R")


# BFS Traversal
def BFS(root):
    queue = [root]

    while queue:
        current = queue.pop(0)
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)


# DFS Traversal
def DFS(root):
    if root:
        print(root.data, end=" ")
        DFS(root.left)
        DFS(root.right)


print("===== BINARY TREE: JAVIER =====")

print("\nBFS Traversal:")
BFS(root)

print("\n\nDFS Traversal:")
DFS(root)

print()
