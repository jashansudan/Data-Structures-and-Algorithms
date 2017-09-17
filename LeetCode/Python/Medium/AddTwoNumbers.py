class Solution(object):
    def addTwoNumber(self, l1, l2):
        newList = ListNode(0)
        newHead = newList
        carry = 0

        while l1 is not None or l2 is not None:
            nodeSum = carry
            carry = 0

            if l1 is not None:
                nodeSum += l1.val
                l1 = l1.next

            if l2 is not None:
                nodeSum += l2.val
                l2 = l2.next

            if nodeSum > 9:
                carry += 1
                nodeSum = nodeSum % 10

            newHead.next = ListNode(nodeSum)
            newHead = newHead.next

        if carry:
            newHead.next = ListNode(1)

        return newList.next
