# ASSESSMENT 3.5: DFS METHOD IN TREE (POSTORDER)
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


# PostOrder Traversal (Left -> Right -> Root)
def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end=" ")


# Display Results
print("========================================")
print("   POSTORDER TRAVERSAL - JESLIE JAVIER")
print("========================================")
print("\nPostOrder (Left -> Right -> Root):")
post_order(root)
print("\n========================================")