import Queue

class Solution(object):
    def findBottomLeftValue(self, root):
        if not root:
            return root
        q = Queue.Queue()
        q.put(root)
        leftMost = root.val
        while not q.empty():
            size = q.qsize()
            while size > 0:
                curr = q.get()
                if curr.right:
                    q.put(curr.right)
                if curr.left:
                    q.put(curr.left)
                leftMost = curr.val
                size -= 1
        return leftMost
