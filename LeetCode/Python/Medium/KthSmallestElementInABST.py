class Solution:
    def kthSmallest(self, root, k):
        nodes = []
        self.inorder(root, nodes)
        return nodes[k - 1]

    def inorder(self, root, nodes):
        if not root:
            return
        self.inorder(root.left, nodes)
        nodes.append(root.val)
        self.inorder(root.right, nodes)
