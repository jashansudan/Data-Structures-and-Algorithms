class Solution(object):
    def isSubtree(self, s, t):
        if s is None:
            return False

        if s.val == t.val:
            if self.checkTree(s, t):
                return True

        return self.isSubtree(s.right, t) or self.isSubtree(s.left, t)

    def checkTree(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val == t.val:
            return self.checkTree(s.left, t.left) and self.checkTree(s.right, t.right)
