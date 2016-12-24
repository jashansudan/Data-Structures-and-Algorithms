package Easy;

import java.util.*;

public class PathSum3 {
	
	public static void main(String[] args){
		
	}
	
	public static  int pathSum(TreeNode root, int sum){
		HashMap<Integer, Integer> preSum = new HashMap<Integer, Integer>();
		preSum.put(0, 1);
		
		return helper(root, 0, sum, preSum);
	}
	
	public static int helper(TreeNode root, int sum, int target, HashMap<Integer, Integer> preSum){
		if (root == null){
			return 0;
		}
		sum += root.val;
		int res = preSum.getOrDefault(sum-target, 0);
		preSum.put(sum, preSum.getOrDefault(sum, 0) + 1);
		
		res += helper(root.left, sum, target, preSum) + helper(root.right, sum, target,preSum);
		preSum.put(sum, preSum.get(sum)-1);
		return res;
	}

}
