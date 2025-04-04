def stringify(node):
    if node is None:
        return 'None'
    result = ''
    while node:
        result += str(node.data) + ' -> '
        if node.next is None:
            break
        node = node.next
    result += 'None'
    return result
