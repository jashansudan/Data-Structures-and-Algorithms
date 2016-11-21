package Easy;

public class SumOfLeftLeaves {
	
	
	public static void main(String[] args){
		
	}
	
	public static int sumOfLeftLeaves(TreeNode root){
		if (root == null){
			return 0;
		}
		return sumOfLeftLeavesHelper(root.left, true) + sumOfLeftLeavesHelper(root.right,false);
	}
		
	public static int sumOfLeftLeavesHelper(TreeNode root, boolean isLeft){	
		if (root == null){
			return 0;
		}
		if (root.left == null && root.right == null){
			if (isLeft){
				return root.val;
			}
		}
		return sumOfLeftLeavesHelper(root.left, true) + sumOfLeftLeavesHelper(root.right,false);	
	}
	
	
	
	

}
