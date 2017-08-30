class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if len(nums) < 1:
            return None

        mid = nums.index(max(nums))
        node = TreeNode(nums[mid])
        node.left = self.constructMaximumBinaryTree(nums[0:mid])
        node.right = self.constructMaximumBinaryTree(nums[mid + 1:])

        return node
