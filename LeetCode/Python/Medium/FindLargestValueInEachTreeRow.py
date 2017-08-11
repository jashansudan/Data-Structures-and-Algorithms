class Solution(object):
    def largestValues(self, root):
        result = []
        if (root is None):
            return result
        que = [root]
        while(que):
            currentMax = que[0].val
            newQueue = []
            for node in que:
                for child in (node.left, node.right):
                    if child:
                        newQueue.append(child)
                if (node.val > currentMax):
                    currentMax = node.val
            result.append(currentMax)
            que = newQueue
        return result
