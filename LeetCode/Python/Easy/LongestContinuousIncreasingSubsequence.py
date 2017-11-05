class Solution:
    def findLengthOfLCIS(self, nums):
        max_len = 0
        prev = float("-inf")
        curr = 0
        for i in range(len(nums)):
            if nums[i] > prev:
                curr += 1
                max_len = max(max_len, curr)
            else:
                curr = 1
            prev = nums[i]
        max_len = max(max_len, curr)
        return max_len
