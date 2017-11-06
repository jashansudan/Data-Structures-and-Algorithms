class Solution:
    def sortColors(self, nums):
        start = 0
        end = len(nums) - 1
        i = 0
        while i <= end:
            if nums[i] == 0 and i != start:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1
            elif nums[i] == 2:
                nums[end], nums[i] = nums[i], nums[end]
                end -= 1
            else:
                i += 1
        return