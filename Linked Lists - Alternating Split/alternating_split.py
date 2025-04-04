class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class Context:
    def __init__(self, first, second):
        self.first = first
        self.second = second
def alternating_split(head):
    if not head or not head.next: 
        raise Exception("List must contain at least two nodes")
    odd_head = odd_tail = head
    even_head = even_tail = head.next
    current = head.next.next
    toggle = True
    while current:
        if toggle:
            odd_tail.next = current
            odd_tail = odd_tail.next
        else:
            even_tail.next = current
            even_tail = even_tail.next
        current = current.next
        toggle = not toggle
    odd_tail.next = None
    even_tail.next = None
    return Context(odd_head, even_head)
