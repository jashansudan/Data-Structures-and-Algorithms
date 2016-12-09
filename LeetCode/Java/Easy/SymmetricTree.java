package Easy;

public class SymmetricTree {

	public static void main(String[] args) {

	}
	
	public static boolean isSymmetric(TreeNode root){
		if (root == null){
			return true;
		}
		return isSymmetricHelper(root.right,root.left);
	}
	
	public static boolean isSymmetricHelper(TreeNode right, TreeNode left){
		if (right == null && left == null){
			return true;
		}
		if (right == null || left == null){
			return false;
		}
		
		if (right.val != left.val){
			return false;
		}
		
		return isSymmetricHelper(right.right, left.left) && isSymmetricHelper(right.left, left.right);
	}

}
