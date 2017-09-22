from ListNode import ListNode


class LinkedList:

    def __init__(self):
        self.head = None
        self.ptr = None
        return

    def add(self, val):
        if self.head is None:
            self.head = ListNode(val)
            self.ptr = self.head
        else:
            self.ptr.next = ListNode(val)
            self.ptr = self.ptr.next
        return

    def printList(self):
        tempPtr = self.head
        while tempPtr is not None:
            print tempPtr.val
            tempPtr = tempPtr.next
        return
