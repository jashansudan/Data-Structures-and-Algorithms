import math


class Solution(object):
    def constructRectangle(self, area):
        low = high = int(math.sqrt(area))
        while (low * high != area):
            if (low * high > area):
                low -= 1
            else:
                high += 1
        return sorted([low, high]).reverse
