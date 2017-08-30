class Solution(object):
    def hasPathSum(self, root, sum):
        if root is None:
            return False

        return self.pathSumHelper(root, sum, 0)

    def pathSumHelper(self, root, sum, curr):
        if root is None:
            return False
        if root.left is None and root.right is None:
            if curr + root.val == sum:
                return True

        left = self.pathSumHelper(root.left, sum, curr + root.val)
        right = self.pathSumHelper(root.right, sum, curr + root.val)
        return left or right
