class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
def remove_duplicates(head):
    if not head:
        return None
    current = head
    while current.next:
        try:
            while current.data == current.next.data:
                current.next = current.next.next
        except AttributeError:
            break
        current = current.next
    return head
