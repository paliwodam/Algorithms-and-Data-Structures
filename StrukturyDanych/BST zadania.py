class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.subtree = None


def subtree_len(root):
    if root is None:
        return 0

    root.subtree = subtree_len(root.left) + subtree_len(root.right) + 1
    return root.subtree


def nie_chce_cie(root, i):
    while i != 0:
        if root.left is None:
            L = 0
        else:
            L = root.left.subtree

        if L >= i:
            root = root.left
        elif L < i - 1:
            i -= (1 + L)
            root = root.right
        else:
            break

    return root


def Michal_nie_wymyslil_nazwy(root):

    i = 1
    if root.left is not None:
        i = root.left.subtree

    while root.parent is not None and root.parent.right is not root:
        root = root.parent
    i -= root.subtree

    while root.parent is not None and root.parent.left is not root:
        root = root.parent
    i += root.subtree


root = BSTNode(1)
root.left = BSTNode(2)
root.right = BSTNode(3)
root.left.left = BSTNode(4)
root.left.right = BSTNode(5)


#  Constructed binary tree is
#             1
#           /   \
#          2     3
#        /  \
#       4    5

