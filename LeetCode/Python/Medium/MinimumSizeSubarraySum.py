class Solution:
    def minSubArrayLen(self, s, nums):
        result = float("inf")
        if not nums:
            return 0

        start = 0
        end = 0
        curr = 0
        while end < len(nums):
            curr += nums[end]
            end += 1
            while curr >= s:
                result = min(result, end - start)
                curr -= nums[start]
                start += 1
        return 0 if result == float("inf") else result
