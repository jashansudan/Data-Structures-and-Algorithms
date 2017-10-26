class Solution:
    def trap(self, height):
        water = 0
        if not height:
            return water
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]

        while (left < right):
            if height[left] < height[right]:
                water += min(leftMax, rightMax) - height[left]
                left += 1
                leftMax = max(leftMax, height[left])
            else:
                water += min(leftMax, rightMax) - height[right]
                right -= 1
                rightMax = max(rightMax, height[right])
        return water
