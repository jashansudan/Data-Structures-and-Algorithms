class Solution:
    def threeSum(self, nums):
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        for low in range(len(nums) - 2):
            if low > 0 and nums[low] == nums[low - 1]:
                continue
            moving_low = low + 1
            high = len(nums) - 1
            while moving_low < high:
                current_sum = nums[low] + nums[moving_low] + nums[high]
                if current_sum == 0:
                    result.append([nums[low], nums[moving_low], nums[high]])
                    moving_low += 1
                    high -= 1
                    while moving_low < high and nums[moving_low] == nums[moving_low - 1]:
                        moving_low += 1
                    while moving_low < high and nums[high] == nums[high + 1]:
                        high -= 1
                elif current_sum > 0:
                    high -= 1
                else:
                    moving_low += 1
        return result
