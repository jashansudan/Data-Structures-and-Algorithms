class Solution:
    def findPeakElement(self, nums):
        start = 0
        end = len(nums) - 1
        while start < end:
            mid1 = (start + end) / 2
            mid2 = mid1 + 1
            if nums[mid1] > nums[mid2]:
                end = mid1
            elif nums[mid2] > nums[mid1]:
                start = mid2
            else:
                return mid1
        return start
