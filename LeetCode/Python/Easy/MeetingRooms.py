class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x.start)

        prev = 0
        for i in range(len(intervals)):
            if intervals[i].start < prev:
                return False
            prev = intervals[i].end
        return True
