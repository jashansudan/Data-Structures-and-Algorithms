class Solution:
    def mergeKLists(self, lists):
        minHeap = []
        sortedList = ListNode(0)
        head = sortedList
        for list in lists:
            if list is not None:
                heapq.heappush(minHeap, (list.val, list))

        while minHeap:
            minVal = heapq.heappop(minHeap)
            sortedList.next = minVal[1]
            sortedList = sortedList.next
            if minVal[1].next is not None:
                heapq.heappush(minHeap, (minVal[1].next.val, minVal[1].next))

        return head.next