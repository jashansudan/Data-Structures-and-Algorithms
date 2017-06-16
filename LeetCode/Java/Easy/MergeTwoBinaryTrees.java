package Easy;

public class MergeTwoBinaryTrees {
	
	public static void main(String[] args){
		
	}
	
	public TreeNode mergeTrees(TreeNode t1, TreeNode t2){
		TreeNode head = mergeNode(t1, t2);
		
		return head;
	}
	
	public TreeNode mergeNode(TreeNode node1, TreeNode node2){
		if (node1 == null && node2 == null){
			return null;
		}
		
		int val = 0;
		if (node1 != null){
			val += node1.val;
		}
		if (node2 != null){
			val += node2.val;
		}
		
		TreeNode current = new TreeNode(val);
		
		current.left = mergeNode(node1 != null? node1.left: null, node2 != null? node2.left:null);
		current.right = mergeNode(node1 != null? node1.right:null, node2 != null? node2.right:null);
		
		return current;
		
	}

}
