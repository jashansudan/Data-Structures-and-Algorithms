class Solution(object):
    def twoSum(self, nums, target):
        numMap = {}
        for i in range(len(nums)):
            if target - nums[i] in numMap:
                return [numMap[target - nums[i]], i]
            else:
                numMap[nums[i]] = i
        return [-1, -1]
