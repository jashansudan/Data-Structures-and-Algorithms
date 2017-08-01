class Solution(object):
    def isPalindrome(self, head):
        fast, slow = head
        while (fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        if (fast is not None):
            slow = slow.next
        slow = self.reverseList(slow)
        fast = head

        while (slow is not None):
            if(fast.val != slow.val):
                return False
            fast = fast.next
            slow = slow.next

    def reverseList(self, head):
        prev = None
        while (head is not None):
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
