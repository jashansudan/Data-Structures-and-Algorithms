import math


class Solution(object):
    def integerBreak(self, n):
        product = 1
        while (n > 7):
            n -= 3
            product *= 3
        product *= n // 2
        product *= n - (n // 2)
        return product
