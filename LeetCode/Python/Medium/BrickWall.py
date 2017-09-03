class Solution(object):
    def leastBricks(self, wall):
        lengthMap = collections.Counter()
        maxBricks = 0
        edge = sum(wall[0])
        for row in wall:
            start = 0
            for brick in row:
                start += brick
                if start == edge:
                    continue
                lengthMap[start] += 1
                maxBricks = max(lengthMap[start], maxBricks)

        return len(wall) - maxBricks
