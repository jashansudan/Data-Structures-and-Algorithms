class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()

        i, maxDistance = 0, 0
        for house in houses:
            while (i < len(heaters) - 1 and
                    abs(heaters[i] - house) >= abs(heaters[i + 1] - house)):
                i += 1
            maxDistance = max(maxDistance, abs(heaters[i] - house))

        return maxDistance
