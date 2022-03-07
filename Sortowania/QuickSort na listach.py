from random import randint, seed


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def quickSort(first):
    if first is None or first.next is None:
        return first, first

    pivot = first
    curr = first.next

    left = Node()
    middle = pivot
    right = Node()

    middle.next = None

    while curr is not None:
        tmp = curr.next

        if curr.value < pivot.value:
            curr.next = left.next
            left.next = curr

        elif curr.value == pivot.value:
            curr.next = middle
            middle = curr

        elif curr.value > pivot.value:
            curr.next = right.next
            right.next = curr
        curr = tmp

    firstLeft, lastLeft = quickSort(left.next)
    firstRight, lastRight = quickSort(right.next)

    if lastLeft is None:
        firstLeft = middle
    else:
        lastLeft.next = middle

    # pivot jest ostatnim elementem środka
    if firstRight is None:
        lastRight = pivot
    else:
        pivot.next = firstRight

    return firstLeft, lastRight


def qsort(L):
    L, _ = quickSort(L)
    return L


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]
L = tab2list(T)

print("przed sortowaniem: L =", end=" ")
printlist(L)
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L

while P.next != None:
    if P.value > P.next.value:
        print("Błąd sortowania")
        exit(0)
    P = P.next

print("OK")
