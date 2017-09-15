class Solution(object):
    def pathSum(self, root, sum):
        result = []
        if root is None:
            return result

        def pathSumHelper(root, sum, curr):
            if root is None:
                return
            if root.left is None and root.right is None:
                if sum - root.val == 0:
                    curr.append(root.val)
                    result.append(curr)
                    return
            else:
                if root.left is not None:
                    pathSumHelper(root.left, sum - root.val, curr + [root.val])
                if root.right is not None:
                    pathSumHelper(root.right, sum - root.val, curr + [root.val])
                return
        pathSumHelper(root, sum, [])
        return result
