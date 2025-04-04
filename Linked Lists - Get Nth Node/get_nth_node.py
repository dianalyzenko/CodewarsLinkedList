class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
def get_nth(node, index):
    if node is None:
        raise TypeError("Invalid index")
    if index < 0:
        raise ValueError("Invalid index")
    for _ in range(index):
        if node.next is None:
            raise ValueError("Invalid index")
        node = node.next
    return node
