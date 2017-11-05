class Codec:

    def serialize(self, root):
        if root is None:
            return "Null"
        else:
            left = self.serializeHelper(root.left)
            right = self.serializeHelper(root.right)
            return str(root.val) + " " + left + " " + right

    def deserialize(self, data):
        nodes = data.split()
        root = self.deserializeHelper(nodes)
        return root

    def deserializeHelper(self, nodes):
        if nodes is None:
            return None
        else:
            if nodes[0] == "Null":
                nodes.pop(0)
                return None
            curr = TreeNode(int(nodes[0]))
            nodes.pop(0)
            curr.left = self.deserializeHelper(nodes)
            curr.right = self.deserializeHelper(nodes)
            return curr
