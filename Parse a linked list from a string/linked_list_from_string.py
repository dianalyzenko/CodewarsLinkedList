class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def linked_list_from_string(s):
    nodes = s.split(" -> ")
    head = None
    current = None
    for node_value in nodes:
        if node_value != "None":
            new_node = Node(int(node_value))
            if not head:
                head = new_node
                current = head
            else:
                current.next = new_node
                current = current.next
    return head
