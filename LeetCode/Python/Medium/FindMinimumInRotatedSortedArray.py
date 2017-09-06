class Solution(object):
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) / 2

            if nums[mid] < nums[start] and nums[mid] < nums[end]:
                start, end = start + 1, mid
            elif nums[mid] > nums[end] and nums[end] < nums[start]:
                start = mid + 1
            else:
                end = mid

        return nums[start]
