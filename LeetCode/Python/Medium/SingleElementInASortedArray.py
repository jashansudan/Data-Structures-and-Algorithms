class Solution(object):
    def singleNonDuplicate(self, nums):
        mask = 0
        for num in nums:
            mask = mask ^ num
        return mask
