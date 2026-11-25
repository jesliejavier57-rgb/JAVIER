# ASSESSMENT 3.5: DFS METHOD IN TREE (INORDER)
# BINARY TREE USING FIRST NAME AND LAST NAME: JESLIE JAVIER


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


# InOrder Traversal (Left -> Root -> Right)
def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end=" ")
    in_order(node.right)


# Display Results
print("========================================")
print("    INORDER TRAVERSAL - JESLIE JAVIER")
print("========================================")
print("\nInOrder (Left -> Root -> Right):")
in_order(root)
print("\n========================================")