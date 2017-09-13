class Solution(object):
    def subsetsWithDup(self, nums):
        result = []

        nums.sort()
        self.subsetsHelper(nums, [], result, 0)
        return result

    def subsetsHelper(self, nums, curr, result, index):
        result.append(curr)

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.subsetsHelper(nums, curr + [nums[i]], result, i + 1)

        return
