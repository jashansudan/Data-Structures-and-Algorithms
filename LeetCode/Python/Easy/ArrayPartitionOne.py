class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum
