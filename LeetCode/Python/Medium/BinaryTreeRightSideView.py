class Solution(object):
    def rightSideView(self, root):
        result = []
        self.rightView(root, result, 0)
        return result

    def rightView(self, root, result, depth):
        if root is None:
            return

        if len(result) == depth:
            result.append(root.val)

        self.rightView(root.right, result, depth + 1)
        self.rightView(root.left, result, depth + 1)
        return
