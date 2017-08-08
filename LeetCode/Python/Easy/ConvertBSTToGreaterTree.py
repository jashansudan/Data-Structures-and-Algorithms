class Solution(object):
    greater = 0

    def convertBST(self, root):
        if root is None:
            return root
        self.convertBST(root.right)
        self.greater += root.val
        root.val = self.greater
        self.convertBST(root.left)
        return root
