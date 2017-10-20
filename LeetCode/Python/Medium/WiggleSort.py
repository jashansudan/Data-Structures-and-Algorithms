class Solution:
    def wiggleSort(self, nums):
        wiggleUp = True
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1] and wiggleUp:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            elif nums[i] <= nums[i + 1] and not wiggleUp:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            wiggleUp = not wiggleUp
        return
