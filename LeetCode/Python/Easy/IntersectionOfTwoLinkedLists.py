class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        lenHeadA = 1
        lenHeadB = 1
        ptrA = headA
        ptrB = headB

        while ptrA.next is not None or ptrB.next is not None:
            if ptrA.next is not None:
                lenHeadA += 1
                ptrA = ptrA.next
            if ptrB.next is not None:
                lenHeadB += 1
                ptrB = ptrB.next

        if ptrA != ptrB:
            return None

        ptrA = headA
        ptrB = headB
        while lenHeadA > lenHeadB:
            ptrA = ptrA.next
            lenHeadA -= 1
        while lenHeadB > lenHeadA:
            ptrB = ptrB.next
            lenHeadB -= 1

        while ptrA != ptrB:
            ptrA = ptrA.next
            ptrB = ptrB.next

        return ptrA
