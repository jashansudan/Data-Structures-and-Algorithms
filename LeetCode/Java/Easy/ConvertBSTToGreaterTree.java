package Easy;

public class ConvertBSTToGreaterTree {
	
	public static void main(String[] args){
		
	}
	
	public int sum = 0;
	
	public TreeNode convertBST(TreeNode root){
		
		convertBSTHelper(root);
		return root;
	}
	
	public void convertBSTHelper(TreeNode root){
		if (root == null) return;
		if (root.right != null){
			convertBSTHelper(root.right);
		}
		root.val += sum;
		sum = root.val;
		if (root.left != null){
			convertBSTHelper(root.left);
		}
	}
	
}
