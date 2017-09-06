class Solution(object):
    def increasingTriplet(self, nums):
        low1 = low2 = float('inf')

        for num in nums:
            if num <= low1:
                low1 = num
            elif num <= low2:
                low2 = num
            else:
                return True
        return False
