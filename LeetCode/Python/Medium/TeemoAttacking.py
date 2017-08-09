class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        totalTime = 0
        prev = float("-inf")
        for time in timeSeries:
            if (prev <= time):
                if (prev + duration <= time):
                    totalTime += duration
                else:
                    totalTime += time - prev
                prev = time
        return totalTime
