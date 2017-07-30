class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        i = result = 0
        for house in houses:
            while (i < len(heaters) - 1 and
                   heaters[i] + heaters[i + 1] <=
                   house * 2):
                i += 1
            result = max(result, abs(heaters[i], house))
        return result
