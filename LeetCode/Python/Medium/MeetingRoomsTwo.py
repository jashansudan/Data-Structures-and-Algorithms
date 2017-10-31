class Solution:
    def minMeetingRooms(self, intervals):
        min_heap = []
        meeting_rooms = 0
        heap_size = 0
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals)):
            if min_heap:
                while min_heap and min_heap[0] <= intervals[i].start:
                    heapq.heappop(min_heap)
                    heap_size -= 1
            heapq.heappush(min_heap, intervals[i].end)
            heap_size += 1
            meeting_rooms = max(meeting_rooms, heap_size)
        return meeting_rooms
