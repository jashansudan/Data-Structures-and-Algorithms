class Solution:
    def longestConsecutive(self, root):
        if root is None:
            return 0
        left = self.longest(root.left, 1, root.val)
        right = self.longest(root.right, 1, root.val)

        return max(left, right)

    def longest(self, root, length, prev):
        if root is None:
            return length
        if root.val != prev + 1:
            left = self.longest(root.left, 1, root.val)
            right = self.longest(root.right, 1, root.val)
            maxOfSubtree = max(left, right)
            return max(maxOfSubtree, length)
        left = self.longest(root.left, length + 1, root.val)
        right = self.longest(root.right, length + 1, root.val)
        return max(left, right)
