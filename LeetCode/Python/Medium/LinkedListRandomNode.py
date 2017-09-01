class Solution(object):
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        ptr = self.head
        val = ptr.val
        length = 1

        while ptr.next is not None:
            ptr = ptr.next
            length += 1
            if random.random() < 1.0 / length:
                val = ptr.val

        return val
