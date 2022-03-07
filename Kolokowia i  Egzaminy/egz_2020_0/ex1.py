from collections import deque


def tanagram(x, y, t):
    positions = [deque() for _ in range(26)]
    for i, c in enumerate(y):
        positions[ord(c)-97].append(i)
    for i, c in enumerate(x):
        closest = positions[ord(c)-97].popleft()
        print(f"closet {c} is on {closest}")
        if abs(closest - i) > t:
            return False
    return True


print(tanagram("kotomysz", "tokmysoz", 2))