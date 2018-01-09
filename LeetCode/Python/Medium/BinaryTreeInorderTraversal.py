class Solution:
    def inorderTraversal(self, root):
        result = []
        stk = []
        curr_node = root
        while stk or curr_node:
            while curr_node:
                stk.append(curr_node)
                curr_node = curr_node.left
            curr_node = stk.pop()
            result.append(curr_node.val)
            curr_node = curr_node.right
        return result
