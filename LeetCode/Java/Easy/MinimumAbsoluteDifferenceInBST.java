package Easy;

import java.util.ArrayList;

public class MinimumAbsoluteDifferenceInBST {
	
	public static void main (String[] args){
		
	}
	//want to find minimum  difference between nodes
	
	public static int getMinimumDifference(TreeNode root){
		ArrayList<Integer> arrList = new ArrayList<Integer>();
		
		getDiff(root, arrList);
		int maxDiff = 100000;
		for (int i =0; i <arrList.size()-1; i++){
			if (Math.abs(arrList.get(i) -arrList.get(i+1)) < maxDiff){
				maxDiff = Math.abs(arrList.get(i) -arrList.get(i+1));
			}
		}
		return maxDiff;
	}
	
	public static void getDiff(TreeNode root, ArrayList<Integer> arrList){
		if (root == null){
			return;
		}
		getDiff(root.left, arrList);
		arrList.add(root.val);
		getDiff(root.right, arrList);
	}
	


}
