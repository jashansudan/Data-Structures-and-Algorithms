package Easy;

import java.util.*;

public class BinaryTreeLevelOrderTraversal {

	public static void main(String[] args) {

	}
	
	public List<List<Integer>> levelOrder(TreeNode root){
		Queue<TreeNode> queue = new LinkedList<TreeNode>();
		List<List<Integer>> traversal = new LinkedList<List<Integer>>();
		
		if (root == null){
			return traversal;
		}
		
		queue.offer(root);
		while(!queue.isEmpty()){
			int levelNum = queue.size();
			List<Integer> levelList = new LinkedList<Integer>();
			for (int i = 0; i < levelNum; i++){
				if (queue.peek().left != null){
					queue.offer(queue.peek().left);
				}
				if (queue.peek().right != null){
					queue.offer(queue.peek().right);
				}
				levelList.add(queue.poll().val);
			}
			traversal.add(levelList);
		}
		return traversal;
	}

}
