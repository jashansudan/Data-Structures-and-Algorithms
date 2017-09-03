class Solution(object):
    def preOrderTraversal(self, root):
        stk = []
        curr = root
        result = []
        while curr is not None or len(stk) > 0:
            while curr is not None:
                result.append(curr.val)
                stk.append(curr)
                curr = curr.left

            stk.pop()
            curr = curr.right

        return result
