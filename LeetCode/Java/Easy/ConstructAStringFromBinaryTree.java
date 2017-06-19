package Easy;

public class ConstructAStringFromBinaryTree {

	public static void main(String[] args){
		
	}
	
	public String tree2str(TreeNode t){
		if (t == null) return "";
		
		String result = t.val + "";
		
		String left = tree2str(t.left);
		String right = tree2str(t.right);
		
		if (left == "" && right == "") return result;
		if (left == "") return result + "()" + "(" + right + ")";
		if (right == "" ) return result + "(" + left + ")";
		return result + "(" + left + ")" + "(" + right + ")";
	}
}
