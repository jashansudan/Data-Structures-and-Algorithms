package Easy;

public class ConvertSortedArrayToBinarySearchTree {

	public static void main(String[] args) {

	}
	
	public TreeNode sortedArrayToBST(int[] nums){
        if (nums.length < 1){
			return null;
		}
        
		TreeNode root = makeTree(nums, 0, nums.length-1);
		return root;
	}
	
	public TreeNode makeTree(int[] nums, int low, int high){
		if (low > high){
			return null;
		}
		int mid = (low + high)/2;
		TreeNode node= new TreeNode(nums[mid]);
		node.left = makeTree(nums, low, mid -1);
		node.right = makeTree(nums, mid + 1, high);
		return node;
	}
	// get a node, make your left middle, the left mid, make your right middle the middle
	//

}
