class Solution:
    def findTarget(self, root, k):
        val_map = {}
        return self.inorder(root, k, val_map)

    def inorder(self, root, k, val_map):
        if root is None:
            return

        left = self.inorder(root.left, k, val_map)
        right = self.inorder(root.right, k, val_map)
        if k - root.val in val_map or left or right:
            return True
        val_map[root.val] = True
        return False
