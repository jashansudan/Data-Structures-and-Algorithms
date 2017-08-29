class Solution(object):
    def isBalanced(self, root):
        if self.isBalancedHelper(root) == -1:
            return False
        return True

    def isBalancedHelper(self, root):
        if root is None:
            return 0

        left = self.isBalancedHelper(root.left)
        right = self.isBalancedHelper(root.right)

        if left == -1 or right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1
