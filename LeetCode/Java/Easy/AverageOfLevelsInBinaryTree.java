package Easy;

import java.util.*;

public class AverageOfLevelsInBinaryTree {
	
	public static void main (String[] args){
		
		
	}
	
	public List<Double> averageOfLevels(TreeNode root) {
		ArrayList<Double> result = new ArrayList<Double>();
		if (root == null) return result;
		Queue<TreeNode> que = new LinkedList<TreeNode>();
		que.offer(root);
		while (!que.isEmpty()){
			double count = que.size();
			double sum = 0;
			for (int i = 0; i < count; i++){
				TreeNode node = que.poll();
				if (node.left != null) que.offer(node.left);
				if (node.right != null) que.offer(node.right);
				sum += node.val;
			}
			result.add(sum/count);
		}
		
		return result;
	}
}
