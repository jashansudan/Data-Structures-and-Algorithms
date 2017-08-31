class Solution(object):
    def optimalDivision(self, nums):
        string = str(nums[0])

        for i in range(1, len(nums)):
            if i == 1 and len(nums) > 2:
                string = string + '/(' + str(nums[i])
            else:
                string = string + '/' + str(nums[i])

        return string + ')' if len(nums) > 2 else string
