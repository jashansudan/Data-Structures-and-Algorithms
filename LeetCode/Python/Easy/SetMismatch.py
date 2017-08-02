class Solution(object):
    def findErrorNums(self, nums):
        result = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                result.append(abs(nums[i]))
                continue
            nums[abs(nums[i]) - 1] = nums[abs(nums[i]) - 1] * -1
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result
