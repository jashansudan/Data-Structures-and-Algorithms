class Solution(object):
    def findSubsequences(self, nums):
        result = []
        self.subsequences(nums, 0, result, [])
        return result

    def subsequences(self, nums, index, result, curr):
        if len(curr) > 1:
            result.append(curr)

        visited = set()

        for i in range(index, len(nums)):
            if not curr or curr[-1] <= nums[i]:
                if nums[i] not in visited:
                    self.subsequences(nums, i + 1, result, curr + [nums[i]])
                    visited.add(nums[i])
        return
