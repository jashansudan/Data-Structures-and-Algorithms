class Solution(object):
    def findDuplicates(self, nums):
        doubles = []
        for i in range(len(nums)):
            if (nums[abs(nums[i]) - 1] < 0):
                doubles.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
        return doubles
