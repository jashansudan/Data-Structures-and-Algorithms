class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head = ListNode(0)
        ptr = head
        while (l1 is not None and l2 is not None):
            if l1.val < l2.val:
                ptr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                ptr.next = ListNode(l2.val)
                l2 = l2.next
            ptr = ptr.next

        if l1 is None:
            ptr.next = l2
        if l2 is None:
            ptr.next = l1

        return head.next
