package Easy;

public class FindModeInBinarySearchTree {

	public static void main(String[] args) {

	}
	
	private int currCount = 0;
	private int maxCount = 0;
	private int currVal = 0;
	private int numberOfModes = 0;
	private int[] modes;
	
	public int[] findMode(TreeNode root){
		
		inOrderTraversal(root);
		modes = new int[numberOfModes];
		numberOfModes = 0;
		currCount = 0;
		inOrderTraversal(root);
		
		return modes;
	}
	
	public void inOrderTraversal(TreeNode root){
		if (root == null){
			return;
		}
		inOrderTraversal(root.left);
		checkCount(root.val);
		inOrderTraversal(root.right);
	}
	
	public void checkCount(int val){
		if (val != currVal){
			currCount = 0;
			currVal  = val;
		}
		currCount++;
		if (val == currVal){
			currCount++;
			if (currCount > maxCount){
				maxCount = currCount;
				numberOfModes = 1;
			} else if (currCount == maxCount){
				if (modes != null){
					modes[numberOfModes] = currVal;
				}
				numberOfModes++;
			}
		}
	}
	

	

}
