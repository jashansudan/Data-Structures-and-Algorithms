class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0

        return self.minDepthHelper(root)

    def minDepthHelper(self, root):
        if root.left is None and root.right is None:
            return 1

        left = self.minDepthHelper(root.left) if root.left is not None else float('inf')
        right = self.minDepthHelper(root.right) if root.right is not None else float('inf')

        return min(left, right) + 1
