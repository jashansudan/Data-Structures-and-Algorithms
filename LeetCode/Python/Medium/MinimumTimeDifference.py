class Solution(object):
    def findMinDifference(self, timePoints):
        for i in range(len(timePoints)):
            timePoints[i] = self.timeAferMidnight(timePoints[i])
        timePoints.sort()
        minDiff = float('inf')

        for i in range(1, len(timePoints)):
            minDiff = min(timePoints[i] - timePoints[i - 1], minDiff)

        minDiff = min(1440 - timePoints[len(timePoints) - 1] + timePoints[0],
                      minDiff)

        return minDiff

    def timeAferMidnight(self, time):
        splitTime = time.split(':')
        total = int(splitTime[1]) + int(splitTime[0]) * 60
        return total
