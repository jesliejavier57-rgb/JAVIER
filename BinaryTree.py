# ASSESSMENT 3.5: DFS METHOD IN TREE (BINARY TREE STRUCTURE)
# BINARY TREE USING FIRST NAME AND LAST NAME: JESLIE JAVIER

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Creating Binary Tree (Level-Order: J E S L I E J A V I E R)
#                J
#              /   \
#             E     S
#            / \   / \
#           L   I E   J
#          / \ / \ /
#         A  V I E R

root = Node("J")
root.left = Node("E")
root.right = Node("S")

root.left.left = Node("L")
root.left.right = Node("I")
root.right.left = Node("E")
root.right.right = Node("J")

root.left.left.left = Node("A")
root.left.left.right = Node("V")
root.left.right.left = Node("I")
root.left.right.right = Node("E")
root.right.left.left = Node("R")


# Display Binary Tree Nodes (Level by Level)
def display_tree(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        current = queue.popleft()
        left_val = current.left.data if current.left else "None"
        right_val = current.right.data if current.right else "None"
        print(f"Node: {current.data}  |  Left: {left_val}  |  Right: {right_val}")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


# Display Results
print("==============================================")
print("   BINARY TREE STRUCTURE - JESLIE JAVIER")
print("==============================================\n")
display_tree(root)
print("\n==============================================")