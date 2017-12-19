class LRUCache:
    def __init__(self, size):
        self.node_map = {}
        self.head = listNode(0, 0)
        self.tail = listNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.max_size = size

    def put(self, k, v):
        if k in self.node_map:
            self.delete(self.node_map[k])
        node = listNode(k, v)
        if len(self.node_map) == self.max_size:
            remove_node = self.head.next
            self.remove(remove_node)
            self.node_map.pop(remove_node.key)
        self.add(node)
        self.node_map[k] = node
        return

    def get(self, key):
        if key in self.node_map:
            temp_node = self.node_map[key]
            self.remove(temp_node)
            self.add(temp_node)
            return temp_node.val
        return -1

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        return

    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail

    def show(self):
        ptr = self.head
        while ptr is not None:
            print ptr.val
            ptr = ptr.next
        return

class listNode:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None
