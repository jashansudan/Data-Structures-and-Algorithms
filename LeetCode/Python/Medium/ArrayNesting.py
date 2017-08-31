class Solution(object):
    def arrayNesting(self, nums):
        if len(nums) < 1:
            return 0

        visited = [False] * len(nums)

        count = 0
        for i in range(len(nums)):
            if not visited[i]:
                index = i
                newCount = 0
                while not visited[index]:
                    newCount += 1
                    visited[index] = True
                    index = nums[index]
                count = max(newCount, count)

        return count
