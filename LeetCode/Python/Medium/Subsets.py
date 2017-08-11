class Solution(object):
    def subsets(self, nums):
        if (nums is None):
            return nums
        result = []
        self.subsetHelper(nums, [], result, 0)
        return result

    def subsetHelper(self, nums, currArray, result, index):
        result.append(currArray)
        for i in range(index, len(nums)):
            self.subsetHelper(nums, currArray + [nums[i]], result, i + 1)
