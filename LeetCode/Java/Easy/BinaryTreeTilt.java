package Easy;

public class BinaryTreeTilt {

	public static void main(String[] args){
		
	}
	
	int result = 0;
	
	public int findTilt(TreeNode root){
		postOrder(root);
		return result;
	}
	
	public int postOrder(TreeNode root){
		if (root == null) return 0;
		
		int left = postOrder(root.left);
		int right = postOrder(root.right);
		
		result += Math.abs(left - right);
		
		return left + right + root.val;
	}
	
}
