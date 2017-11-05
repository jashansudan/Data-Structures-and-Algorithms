class Solution:
    def inorderSuccessor(self, root, p):
        stk = []
        curr = root
        found = False
        while stk or curr:
            while curr is not None:
                stk.append(curr)
                curr = curr.left

            temp = stk.pop()
            if found:
                return temp
            elif temp == p:
                found = True
            curr = temp.right
        return None
