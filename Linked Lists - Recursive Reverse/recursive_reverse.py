class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
def reverse(head):
    if not head or not head.next:
        return head
    reversed_head = reverse(head.next)
    temp_node = reversed_head
    while temp_node.next:
        temp_node = temp_node.next
    temp_node.next = head
    head.next = None
    return reversed_head
