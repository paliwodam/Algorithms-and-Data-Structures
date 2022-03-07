class Node:
    def __init__(self, val, parent=None, max=0, visibility=False):
        self.val = val
        self.left = None
        self.right = None
        self.parent = parent
        self.max = max
        self.visibility = visibility


def add_lego(root, block, id):
    if root is None:
        return 0

    if not root.visibility:
        root.val = block[id]
        root.visibility = True
        root.max += block[2]

        if id == 0:
            root.right = Node(None, root, root.max)
            root.left = Node(None, root)
        else:
            root.right = Node(None, root)
            root.left = Node(None, root, root.max)
        print(root.parent.val, block, block[id], root.max)

        return root.max

    if root.val > block[id]:
        root.max = max(root.max, add_lego(root.left, block, id))
        return root.max
    elif root.val < block[id]:
        root.max = max(root.max, add_lego(root.right, block, id))
        return root.max
    else:
        root.max += block[2]
        return root.max


def lego(A):
    n = len(A)

    root = Node(A[0][0], None, A[0][2], True)
    root.right = Node(A[0][1], root, A[0][2], True)
    root.left = Node(None, root)
    root.right.left = Node(None, root.right, A[0][2])
    root.right.right = Node(None, root.right)
    print(root.max)
    max_ = 0
    for i in range(1, n):

        max_ = add_lego(root, A[i], 1)
        print(max_)
        max_= add_lego(root, A[i], 0)
        print(max_)
    return max_


K = [(1, 3, 1), (2, 5, 2), (0, 3, 2), (8, 9, 3), (4, 6, 1)]
print(lego(K))