class Solution:
    def hindex(self, citations):
        hindex = 0
        min_heap = []
        for i in range(len(citations)):
            if len(min_heap) == 0 and citations[i] > 0 or citations[i] >= hindex:
                heapq.heappush(min_heap, citations[i])
                hindex += 1
                if min_heap[0] < hindex:
                    heapq.heappop(min_heap)
                    hindex -= 1
        return hindex
