# Datastructure - Common Python Datastructures

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head: ListNode):
        self.head = head