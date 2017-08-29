class Solution(object):
    def reverseList(self, head):
        prev = None
        while head is not None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
