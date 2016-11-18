package Easy;

import java.util.*;

public class MaxDepthBinaryTree {

	public static void main(String[] args) {

	}
	
	public int maxDepth(TreeNode node){
		int depth = 0;
		return recMaxDepth(node, depth);
		
	}
	
	public int recMaxDepth(TreeNode node, int depth){
		if (node == null){
			return depth;
		}
		return Math.max(recMaxDepth(node.left, depth+1), recMaxDepth(node.right, depth+1));
	}

}


class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;
	TreeNode(int x) { val = x; }
}
