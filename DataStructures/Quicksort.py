from collections import deque


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def iterativeQuicksort(a):
    stack = deque()

    start = 0
    end = len(a) - 1

    stack.append((start, end))

    while stack:
        start, end = stack.pop()
        pivot = partition(a, start, end)

        if pivot - 1 > start:
            stack.append((start, pivot - 1))
        if pivot + 1 < end:
            stack.append((pivot + 1, end))


