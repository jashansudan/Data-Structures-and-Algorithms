class Solution:
    def plusOne(self, head):

        num = self.helper(head)
        if num == 1:
            new_head = ListNode(1)
            new_head.next = head
            head = new_head
        return head

    def helper(self, head):
        if head is None:
            return 1

        num = self.helper(head.next)
        if num == 1:
            if head.val != 9:
                head.val += 1
                return 0
            else:
                head.val = 0
                return 1
