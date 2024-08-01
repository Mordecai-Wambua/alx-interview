#!/usr/bin/python3
"""Interview question: Lockboxes."""


def canUnlockAll(boxes):
    """Determine if all the boxes can be opened."""
    count = len(boxes)
    unlocked = set()
    queue = set(boxes[0])

    while queue:
        new = queue.pop()
        if new < count and new not in unlocked:
            unlocked.add(new)
            queue.update(boxes[new])

    return len(unlocked) == count
