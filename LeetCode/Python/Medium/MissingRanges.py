class Solution:
    def findMissingRanges(self, nums, lower, upper):
        result = []
        nums.append(upper + 1)
        prev = lower - 1
        for i in nums:
            if i > prev + 2:
                result.append(str(prev + 1) + '->' + str(i - 1))
            elif i == prev + 2:
                result.append(str(prev + 1))
            prev = i
        return result
