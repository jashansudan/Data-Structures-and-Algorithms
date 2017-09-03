class Solution(object):
    def totalHammingDistance(self, nums):
        totalDistance = 0
        mask = 1 << 29

        while mask > 0:
            count = 0
            for num in nums:
                if mask & num > 0:
                    count += 1
            totalDistance += (len(nums) - count) * count

            mask = mask >> 1

        return totalDistance
