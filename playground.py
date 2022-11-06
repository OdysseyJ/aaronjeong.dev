import sys
input = sys.stdin.readline
n = int(input().strip())


class Node:
    value: None
    left: None
    right: None

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class DLinkedList:
    root = Node("root")

    def __init__(self, node):
        node.left = self.root
        self.root.right = node

    def move_left(self, node):
        left_node = node.left
        if left_node == self.root:
            return

        right_node = node.right
        if right_node:
            right_node.left = left_node

        node.right = left_node
        node.left = left_node.left
        if left_node.left:
            left_node.left.right = node

        left_node.right = right_node
        left_node.left = node

    def move_right(self, node):
        if not node.right:
            return
        left_node = node.left
        right_node = node.right
        node.left = right_node

        if left_node:
            left_node.right = right_node

        if right_node:
            node.right = right_node.right
            right_node.left = left_node
            right_node.right = node

    def remove_left(self, node):
        left_node = node.left
        if left_node == self.root:
            return

        node.left = left_node.left
        left_left_node = left_node.left
        if left_left_node:
            left_left_node.right = node

    def add_left(self, node, new_node):
        left_node = node.left
        left_node.right = new_node
        node.left = new_node
        new_node.right = node
        new_node.left = left_node

    def travel(self):
        node = self.root.right
        while node:
            if node.value != 'cur':
                print(node.value, end="")
            node = node.right
        print()


for _ in range(n):
    sentence = input().strip()
    cursor = Node('cur')
    dl = DLinkedList(cursor)
    for s in sentence:
        if s == "<":
            dl.move_left(cursor)
        elif s == ">":
            dl.move_right(cursor)
        elif s == "-":
            dl.remove_left(cursor)
        else:
            dl.add_left(cursor, Node(s))
    dl.travel()