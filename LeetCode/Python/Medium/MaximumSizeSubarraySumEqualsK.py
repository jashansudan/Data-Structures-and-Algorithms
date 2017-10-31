class Solution:
    def maxSubArrayLen(self, nums, k):
        max_len = 0
        sum_map = {}
        sum_map[0] = 0
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum not in sum_map:
                sum_map[running_sum] = i + 1
            if running_sum - k in sum_map:
                max_len = max(i - sum_map[running_sum - k] + 1, max_len)

        return max_len
