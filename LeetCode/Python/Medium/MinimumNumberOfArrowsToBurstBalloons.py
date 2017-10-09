class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[1])
        arrows = 1
        if not points:
            return 0
        firstPoint = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > firstPoint:
                arrows += 1
                firstPoint = points[i][1]
        return arrows
