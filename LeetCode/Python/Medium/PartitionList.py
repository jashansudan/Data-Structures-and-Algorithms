class Solution(object):
    def partition(self, head, x):
        greater = ListNode(0)
        greater_ptr = greater
        less = ListNode(0)
        less_ptr = less
        while head:
            if head.val >= x:
                greater.next = head
                greater = greater.next
            else:
                less.next = head
                less = less.next
            head = head.next
        greater.next = None
        less.next = greater_ptr.next
        return less_ptr.next
