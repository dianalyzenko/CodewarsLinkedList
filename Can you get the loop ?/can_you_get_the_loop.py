def loop_size(node):
    start = node
    end = node
    while end and end.next:
        start = start.next
        end = end.next.next
        if start == end:
            break
    else:
        return 0
    cycle_length = 1
    pointer = start.next
    while pointer != start:
        cycle_length += 1
        pointer = pointer.next
    return cycle_length

