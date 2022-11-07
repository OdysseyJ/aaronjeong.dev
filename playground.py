import sys
from collections import deque

input = sys.stdin.readline

queue = deque([])

new_queue = []


def push(k: int):
    queue.append(k)
    new_queue.append(k)


def pop():
    return queue.popleft()


def front():
    return queue[0]


def back():
    return queue[-1]
