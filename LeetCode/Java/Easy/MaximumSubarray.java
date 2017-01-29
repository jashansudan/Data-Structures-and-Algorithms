package Easy;

public class MaximumSubarray {
	
	public void main(String[] args){
		
	}
	
	public int maxSubArray(int[] nums){
		if (nums.length < 1){
			return 0;
		}
		int maxSoFar = nums[0];
		int currMax = nums[0];
		for (int i = 1; i < nums.length; i++){
			currMax = Math.max(nums[i],currMax+nums[i]);
			maxSoFar= Math.max(maxSoFar, currMax);
		}
		
		return maxSoFar;
	}

}
