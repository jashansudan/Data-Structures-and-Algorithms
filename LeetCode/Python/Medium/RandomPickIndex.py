class Solution(object):

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        count = 0
        index = -1
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                count += 1
                if random.random() < 1 / float(count):
                    index = i
        return index
