package Easy;



public class InvertBinaryTree {

	public static void main(String[] args) {
		

	}
	
	
	public TreeNode invertTree(TreeNode root){
		if (root == null){
			return null;
		}
		TreeNode temp = root.right;
		root.right = root.left;
		root.left = temp;
		invertTree(root.right);
		invertTree(root.left);
		return root;
		
	}
}



