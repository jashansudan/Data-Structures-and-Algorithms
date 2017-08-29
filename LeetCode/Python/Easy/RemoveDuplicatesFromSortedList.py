class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return head

        ptr = head
        while (ptr.next is not None):
            if ptr.next.val == ptr.val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next

        return head
