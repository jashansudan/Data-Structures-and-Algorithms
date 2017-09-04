class Solution(object):
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        evenHead = even

        while(even.next is not None and even.next.next is not None):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        if even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = None

        odd.next = evenHead

        return head
