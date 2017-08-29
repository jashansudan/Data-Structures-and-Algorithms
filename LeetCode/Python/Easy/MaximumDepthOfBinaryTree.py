class Solution(object):
    def maxDepth(self, root):
        return self.maxDepthHelper(root, 0)

    def maxDepthHelper(self, root, count):
        if root is None:
            return count
        else:
            return max(self.maxDepthHelper(root.left, count + 1),
                       self.maxDepthHelper(root.right, count + 1))
