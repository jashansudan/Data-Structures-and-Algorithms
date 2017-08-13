class Solution(object):
    def sumNumbers(self, root):
        sum = 0
        if root is None:
            return sum
        sum = self.sumNumbersHelper(root, "")
        return sum

    def sumNumbersHelper(self, root, path):
        if (root.left is None and root.right is None):
            return int(path + str(root.val))
        sum = 0
        if root.left is not None:
            sum += self.sumNumbersHelper(root.left, sum, path + str(root.val))
        if root.right is not None:
            sum += self.sumNumbersHelper(root.right, sum, path + str(root.val))
        return sum
