from collections import collections


class Solution(object):
    def findPairs(self, nums, k):
        pairs = 0
        numberDict = collections.Counter(nums)
        for i in numberDict:
            if k > 0 and i + k in numberDict or k == 0 and numberDict[i] > 1:
                pairs += 1
        return pairs
