from random import random


class Solution(object):

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        shuffled = self.nums[:]
        for i in range(len(self.nums)):
            rand = random.randint(0, len(self.nums) - 1)
            shuffled[i], shuffled[rand] = shuffled[rand], shuffled[i]
        return shuffled
