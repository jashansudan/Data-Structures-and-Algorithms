package Easy;

public class DiameterOfBinaryTree {
	
	public static void main(String[] args){
		
	}
	
	public int max = 0;
	
	public int diameterOfBinaryTree(TreeNode root){
		
		maxDepth(root);
		return max;
	}

	public int maxDepth(TreeNode root){
		if (root == null) return 0;
		
		int left = maxDepth(root.left);
		int right = maxDepth(root.right);
		
		max = Math.max(max, left + right);
		
		return Math.max(left, right) + 1;
	}
	

}
