class Solution:
    def rob(self, nums):
        not_rob = 0
        rob = 0
        for i in range(len(nums)):
            curr_rob = max(not_rob + nums[i], rob)
            not_rob = rob
            rob = curr_rob
        return max(not_rob, rob)
