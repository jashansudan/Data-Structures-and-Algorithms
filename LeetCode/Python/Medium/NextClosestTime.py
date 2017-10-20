class Solution:
    def nextClosestTime(self, time):
        nums = time[:2] + time[3:]
        permutations = self.perm(nums)
        filteredPerm = self.filterPerm(permutations)
        filteredPerm.sort()

        index = filteredPerm.index(nums)
        if index == len(filteredPerm) - 1:
            return filteredPerm[0][:2] + ":" + filteredPerm[0][2:]
        else:
            return filteredPerm[index + 1][:2] + ":" + filteredPerm[index + 1][2:]

    def perm(self, nums):
        result = []
        self.permHelper(nums, result, "")
        return result

    def permHelper(self, nums, result, curr):
        if len(curr) == len(nums):
            result.append(curr)
        else:
            for i in range(len(nums)):
                self.permHelper(nums, result, curr + nums[i])
        return

    def filterPerm(self, perms):
        result = []
        for i in range(len(perms)):
            curr = perms[i]
            hour = curr[:2]
            minute = curr[2:]
            if 0 <= int(hour) <= 24 and 0 <= int(minute) <= 59:
                if perms[i] not in result:
                    result.append(perms[i])
        return result
