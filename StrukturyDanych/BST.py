from collections import deque


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right

    return None


def find_min(root):
    while root.left:
        root = root.left
    return root


def find_max(root):
    while root.right:
        root = root.right
    return root


def insert(root, key):
    prev = root
    while root is not None:
        prev = root
        if root.key > key:
            root = root.left
        else:
            root = root.right
    if prev.key > key:
        prev.left = BSTNode(key)
        prev.left.parent = prev
    elif prev.key < key:
        prev.right = BSTNode(key)
        prev.right.parent = prev
    else:
        return False
    return True


def insert2(root, key):
    if root.key == key:
        return False
    elif root.key > key:
        if root.left is not None:
            insert2(root.left, key)
        else:
            root.left = BSTNode(key)
            root.left.parent = root
    else:
        if root.right is not None:
            insert2(root.right, key)
        else:
            root.right = BSTNode(key)
            root.right.parent = root


"""
def binary_tree_insert(node, key, value):
    if node == None:
        return NodeTree(None, key, value, None)
    if key == node.key:
        return NodeTree(node.left, key, value, node.right)
    if key < node.key:
        return NodeTree(binary_tree_insert(node.left, key, value), node.key, node.value, node.right)
    return NodeTree(node.left, node.key, node.value, binary_tree_insert(node.right, key, value))
"""


def remove(root, key):
    if root is None:
        return False
    if root.key == key:
        if root.left is not None and root.right is not None:
            pass
        elif root.left is not None:
            pass
        elif root.right is not None:
            pass
        else:
            pass
    elif root.key > key:
        remove(root.left, key)
    elif root.key < key:
        remove(root.right, key)


def predecessor(root):
    if root.left is not None:
        return find_max(root.left)
    else:
        while root.parent is not None and root.parent.key > root.key:
            root = root.parent
        return root.parent


def successor(root):
    if root.right is not None:
        return find_min(root.right)
    else:
        while root.parent is not None and root.parent.key < root.key:
            root = root.parent
        return root.parent


def inorder_tree_walk(root):
    if root is not None:
        inorder_tree_walk(root.left)
        print(root.key)
        inorder_tree_walk(root.right)


def inorder_tree_walk_iter(root):
    stack = deque()
    stack.append(root)

    while True:
        if root is not None:
            stack.append(root)
            root = root.left
        elif stack:
            root = stack.pop()
            print(root.key, end=" ")
            root = root.right
        else:
            break
    print()


def inorder_tree_walk_two(root):
    root = find_min(root)
    while root is not None:
        print(root.key, end=" ")
        root = successor(root)


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

