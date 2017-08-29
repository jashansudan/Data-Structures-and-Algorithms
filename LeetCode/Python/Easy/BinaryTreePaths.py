class Solution(object):
    def binaryTreePaths(self, root):
        result = []
        if root is None:
            return result

        self.binaryTreePathHelper(root, result, '')
        return result

    def binaryTreePathHelper(self, root, result, curr):
        if root.left is None and root.right is None:
            result.append(curr + str(root.val))
        else:
            curr = curr + str(root.val) + '->'
            if root.left is not None:
                self.binaryTreePathHelper(root.left, result, curr)
            if root.right is not None:
                self.binaryTreePathHelper(root.right, result, curr)
