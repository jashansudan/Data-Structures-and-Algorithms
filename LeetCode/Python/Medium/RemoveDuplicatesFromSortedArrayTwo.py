class Solution(object):
    def removeDuplicates(self, nums):
        if (len(nums) < 3):
            return len(nums)
        count = 2
        for i in range(2, len(nums)):
            if (nums[i] != nums[count - 2]):
                nums[count] = nums[i]
                count += 1
        return count
