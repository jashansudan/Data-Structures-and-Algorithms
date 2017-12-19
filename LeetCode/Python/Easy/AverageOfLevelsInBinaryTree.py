class Solution:
    def averageOfLevels(self, root):
        result = []
        if root is None:
            return result
        q = collections.deque()
        q.append(root)
        while q:
            count, size = len(q), len(q)
            level_sum = 0
            while count > 0:
                node = q.popleft()
                level_sum += node.val
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                count -= 1
            result.append(level_sum / float(size))
        return result
