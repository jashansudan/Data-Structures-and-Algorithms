class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == p or root == q:
            return root
        if root is None:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        else:
            if left:
                return left
            if right:
                return right
            else:
                return None
