class Solution(object):
    def addOneRow(self, root, v, d):
        if (d == 1):
            node = TreeNode(v)
            node.left = root
            return node

        self.traverseTree(root, v, d)
        return root

    def traverseTree(self, root, v, d):
        if (root is None):
            return
        if (d - 1 == 1):
            tempLeft = root.left
            tempRight = root.right
            root.right = TreeNode(v)
            root.left = TreeNode(v)
            root.right.right = tempRight
            root.left.left = tempLeft
            return
        else:
            self.traverseTree(root.right, v, d - 1)
            self.traverseTree(root.left, v, d - 1)
            return
