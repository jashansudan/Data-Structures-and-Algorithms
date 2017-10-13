class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        result = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - 1 != nums[i - 1]:
                if nums[i - 1] == start:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(nums[i - 1]))
                start = nums[i]
        if nums[len(nums) - 1] == start:
            result.append(nums[len(nums - 1)])
        else:
            result.append(str(start) + "->" + str(nums[len(nums) - 1]))

        return result
