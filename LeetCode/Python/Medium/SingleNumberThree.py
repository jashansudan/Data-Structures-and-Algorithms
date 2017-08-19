class Solution(object):
    def singleNumber(self, nums):
        xor = 0
        for i in nums:
            xor ^= i
        mask = 1
        while mask & xor < 1:
            mask = mask << 1
        withMask = 0
        withoutMask = 0
        for x in nums:
            if mask & x:
                withMask ^= x
            else:
                withoutMask ^= x
        return [withMask, withoutMask]
