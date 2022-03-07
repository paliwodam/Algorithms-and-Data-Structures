class FastListNode:
    def __init__(self, a):
        self.a = a # przechowywana liczba całkowita
        self.next = [] # lista odsyłaczy do innych elementów; początkowo pusta

    def __str__(self): # zwraca zawartość węzła w postaci napisu
        res = 'a: ' + str(self.a) + '\t' + 'next keys: '
        res += str([n.a for n in self.next])
        return res


def fast_list_prepend(L, a):
    start = FastListNode(a)
    m_len = len(L.next) + 1

    for i in range(m_len):
        nxt = L
        check = True
        for j in range(i, -1, -1):
            if len(nxt.next) < j:
                check = False
                break
            nxt = nxt.next(j)
        if check:
            nxt.next.append(nxt)
    return start