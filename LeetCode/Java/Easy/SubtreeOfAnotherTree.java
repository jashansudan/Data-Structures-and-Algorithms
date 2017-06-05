package Easy;

public class SubtreeOfAnotherTree {
	
	public static void main(String[] args){
		
	}
	
	public static boolean isSubtree(TreeNode s, TreeNode t){	
		if (s == null && t == null){
			return true;
		}
		if (s == null || t== null){
			return false;
		}
		if (s.val == t.val){
			
			return isPerfectSubtree(s,t) || isSubtree(s.left, t) || isSubtree(s.right, t);
		}
		
		return isSubtree(s.left, t) || isSubtree(s.right, t);
	}
	
	public static boolean isPerfectSubtree(TreeNode s, TreeNode t){
		if (s == null && t == null){
			return true;
		}
		if (s == null || t== null){
			return false;
		}
		if (s.val != t.val){
			return false;
		}
		
		return isPerfectSubtree(s.right, t.right) && isPerfectSubtree(s.left, t.left);
	}

}
