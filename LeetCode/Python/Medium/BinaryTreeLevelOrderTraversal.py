class Solution(object):
    def levelOrder(self, root):
        result = []
        if root is None:
            return result
        que = collections.deque()
        que.append(root)
        while que:
            size = len(que)
            temp = []
            while size > 0:
                curr = que.popleft()
                temp.append(curr.val)
                if curr.left is not None:
                    que.append(curr.left)
                if curr.right is not None:
                    que.append(curr.right)
                size -= 1
            result.append(temp)
        return result
