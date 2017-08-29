class Solution(object):
    def sortedArrayToBST(self, nums):
        if nums is None:
            return nums

        return self.makeBinaryTree(nums, 0, len(nums) - 1)

    def makeBinaryTree(self, nums, start, end):
        if start > end:
            return None

        mid = (start + end) / 2
        root = TreeNode(nums[mid])
        root.left = self.makeBinaryTree(nums, start, mid - 1)
        root.right = self.makeBinaryTree(nums, mid + 1, end)

        return root
