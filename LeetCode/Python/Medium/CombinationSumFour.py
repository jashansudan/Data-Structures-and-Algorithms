class Solution:
    def combinationSum4(self, nums, target):
        combs = [0] * (target + 1)
        combs[0] = 1
        for i in range(len(combs)):
            for num in nums:
                if num <= i:
                    combs[i] += combs[i - num]

        return combs[target]
