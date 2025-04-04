from preloaded import Node

def swap_pairs(head):
    if not head or not head.next:
        return head
    placeholder = Node(0)
    placeholder.next = head
    previous, current = placeholder, head
    while current and current.next:
        upcoming_pair = current.next.next
        previous.next = current.next
        current.next.next = current
        current.next = upcoming_pair
        previous = current
        current = upcoming_pair
    return placeholder.next
