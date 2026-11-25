# ASSESSMENT 3.5: DFS METHOD IN TREE (PREORDER)
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


# PreOrder Traversal (Root -> Left -> Right)
def pre_order(node):
    if node is None:
        return
    print(node.data, end=" ")
    pre_order(node.left)
    pre_order(node.right)


# Display Results
print("========================================")
print("   PREORDER TRAVERSAL - JESLIE JAVIER")
print("========================================")
print("\nPreOrder (Root -> Left -> Right):")
pre_order(root)
print("\n========================================")