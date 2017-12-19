class Solution:
    def checkSubarraySUm(self, nums, k):
        num_map = {0: -1}
        accumilator = 0
        for i in range(len(nums)):
            accumilator += nums[i]
            if k != 0:
                accumilator %= k
            if accumilator in num_map and i - num_map[accumilator] > 1:
                return True
            elif accumilator not in num_map:
                num_map[accumilator] = i
        return False
