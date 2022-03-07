class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


def list_to_node(A):
    n = len(A)
    head = Node(A[0])
    curr = head
    for i in range(1, n):
        curr.next = Node(A[i])
        curr = curr.next
    return head


def node_to_list(head):
    A = []
    while head is not None:
        A.append(head.val)
        head = head.next
    return A


# def merge(head1, head2):
#     head = Node(None)
#     curr = head
#     while head1 is not None and head2 is not None:
#         if head1.val < head2.val:
#             curr.next = head1
#             head1 = head1.next
#             curr = curr.next
#         else:
#             curr.next = head2
#             head2 = head2.next
#             curr = curr.next
#
#     if head1 is not None:
#         curr.next = head1
#     if head2 is not None:
#         curr.next = head2
#
#     return head.next


def merge_all(A):
    n = len(A)
    B = []
    cnt = 0
    for i in range(n):
        B.append(list_to_node(A[i]))
        cnt += len(A[i])

    head = Node(None)
    curr = head
    for k in range(cnt):
        min_idx = 0
        while B[min_idx] is None:
            min_idx += 1
        for i in range(n):
            if B[i] is not None and B[min_idx].val > B[i].val:
                min_idx = i
        curr.next = B[min_idx]
        curr = curr.next
        B[min_idx] = B[min_idx].next

    return node_to_list(head.next)


A = [[0, 1, 2, 4, 5], [0, 10, 20], [5, 15, 25]]
print(merge_all(A))
