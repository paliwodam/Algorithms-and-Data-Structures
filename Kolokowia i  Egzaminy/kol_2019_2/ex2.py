class Node:
    def __init__( self ):
        self.children = 0 # liczba dzieci węzła
        self.child = [] # lista par (dziecko, waga krawędzi)
        self.f = 0
        self.g = 0


def heavy_path(root):
    if root.children == 0:
        return 0, 0
    else:
        f_max1 = 0
        f_max2 = 0

        for child, d in root.child:
            f, g = heavy_path(child)
            if f + d > root.f:
                root.f = f + d
            if g > root.g:
                root.g = g

            if f + d > f_max1:
                f_max1 = f + d
            elif f + d > f_max2:
                f_max2 = f + d

        if f_max1 + f_max2 > root.g:
            root.g = f_max1 + f_max2
        return root.f, root.g


T = [[(1, 5), (2, 2), (3, -2)],
     [(4, 2), (5, 7)],
     [],
     [(6, -1)],
     [],
     [],
     [(7, 20), (8, 19)],
     [],
     []]


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
G = Node()
H = Node()
I = Node()


A.children = 3
A.child = [(B, 5), (C, 1), (D, -2)]

B.children = 2
B.child = [(E, 2), (F, 17)]

D.children = 1
D.child = [(G, -1)]

G.children = 2
G.child = [(H, 20), (I, 18)]


f, g = heavy_path(A)
print(g)


