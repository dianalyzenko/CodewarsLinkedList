class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def sorted_insert(head, data):
    new_node = Node(data)
    if head is None or head.data > data:
        new_node.next = head
        return new_node
    current_node = head
    while current_node.next and current_node.next.data < data:
        current_node = current_node.next
    new_node.next = current_node.next
    current_node.next = new_node
    return head