class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            movingStart = start + 1
            while movingStart < end:
                curr = nums[start] + nums[movingStart] + nums[end]
                if curr >= target:
                    end -= 1
                else:
                    count += end - movingStart
                    movingStart += 1
            end = len(nums) - 1
            start += 1
        return count
