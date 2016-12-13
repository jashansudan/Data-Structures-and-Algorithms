package Easy;

public class MinimumDepthOfBinaryTree {

	public static void main(String[] args) {

	}
	
	public static int minDepth(TreeNode root){
		if (root == null){
			return 0;
		}
		return minDepthHelper(root, 1);
	}

	public static int minDepthHelper(TreeNode node, int depth){
		
		if (node.right == null && node.left == null){
			return depth;
		}
		if (node.right == null && node.left != null){
			return minDepthHelper(node.left, depth+1);
		}
		if (node.right != null && node.left == null){
			return minDepthHelper(node.right, depth+1);
		}
		else {
			return Math.min(minDepthHelper(node.right, depth+1), minDepthHelper(node.left, depth+1));
		}
		
		
	}
}
