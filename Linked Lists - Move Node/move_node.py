class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
def move_node(source, dest):
    if source is None and dest is None:
        raise ValueError("")
    moved_node = Node(source.data)
    source = source.next
    moved_node.next = dest
    dest = moved_node
    return Context(source, dest)
