class Solution(object):
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        currentLevel = [root]
        result = []
        while currentLevel:
            nextLevel = []
            temp = []
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                temp.append(node.val)
            if len(result) % 2 == 1:
                temp.reverse()
            result.append(temp)
            currentLevel = nextLevel
        return result
