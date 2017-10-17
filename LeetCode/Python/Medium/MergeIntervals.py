class Solution:
    def merge(self, intervals):
        if len(intervals) < 1:
            return []
        intervals.sort(key=lambda x: x.start)
        result = []
        start = intervals[0].start
        end = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start <= end:
                end = max(intervals[i].end, end)
            else:
                result.append(Interval(start, end))
                start = intervals[i].start
                end = intervals[i].end
        result.append(Interval(start, end))
        return result
