class Solution(object):
    def isValidBST(self, root):
        return self.isValidHelper(root, float('inf'), float('-inf'))

    def isValidHelper(self, root, maxVal, minVal):
        if root is None:
            return True
        if root.val >= maxVal or root.val <= minVal:
            return False
        else:
            left = self.isValidHelper(root.left, root.val, minVal)
            right = self.isValidHelper(root.right, maxVal, root.val)
            return left and right
