class Solution(object):
    def printTree(self, root):
        height = self.getHeight(root)
        if height < 1:
            return 0

        col = 2 ** height - 1
        array = [["" for i in range(col)] for i in range(height)]

        self.insertIntoArray(array, root, 0, col, 0)

        return array


    def getHeight(self, root):
        if root is None:
            return 0

        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1

    def insertIntoArray(self, array, root, left, right, height):
        if root is None:
            return

        mid = (left + right) / 2
        array[height][mid] = str(root.val)

        self.insertIntoArray(array, root.left, left, mid - 1, height + 1)
        self.insertIntoArray(array, root.right, mid + 1, right, height + 1)

        return
