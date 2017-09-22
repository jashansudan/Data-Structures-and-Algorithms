class Solution:
    def hammingWeight(self, n):
        mask = 1
        count = 0
        while n > 0:
            if mask & n:
                count += 1
            n = n >> 1
        return count
