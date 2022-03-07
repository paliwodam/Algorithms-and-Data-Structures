
class BSTNode:
    def __init__(self, key, amount = 0):
        self.key = key
        self.left = None
        self.right = None
        self.amount = amount


def increase(root, key):
    prev = root
    while root is not None:
        prev = root
        if root.key > key:
            root = root.left
        elif root.key < key:
            root = root.right
        else:
            root.amount += 1
            if root.amount == 1:
                return 1
            else:
                return 0

    if prev.key > key:
        prev.left = BSTNode(key, 1)
        return 1

    elif prev.key < key:
        prev.right = BSTNode(key, 1)

        return 1


def reduce(root, key):
    while root is not None:
        if root.key > key:
            root = root.left
        elif root.key < key:
            root = root.right
        else:
            root.amount -= 1
            if root.amount == 0:
                return 1
            else:
                return 0

    return 1


def longest_incomplete(A, l):
    n = len(A)
    root = BSTNode(A[0], 1)

    i = 1
    j = 0

    l -= 1
    d = 1

    while i < n:
        l -= increase(root, A[i])

        while l < 1:
            l += reduce(root, A[j])
            j += 1

        if i-j + 1 > d:
            d = i-j + 1

        i += 1

    return d


# A = [1, 100, 5, 100, 1, 5, 1, 5]
A = [1, 100, 5, 100, 1, 5, 1, 100, 5, 1, 1, 100, 1, 1, 5, 1]
print(longest_incomplete(A, 3))