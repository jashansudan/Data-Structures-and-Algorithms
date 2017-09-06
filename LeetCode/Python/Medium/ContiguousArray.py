class Solution(object):
    def findMaxLength(self, nums):
        sumCounts = collections.Counter()
        sumCounts[0] = -1

        sumSoFar = 0
        maxSeen = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                sumSoFar -= 1
            else:
                sumSoFar += 1
            if sumSoFar in sumCounts:
                maxSeen = max(maxSeen, i - sumCounts[sumSoFar])
            else:
                sumCounts[sumSoFar] = i

        return maxSeen
