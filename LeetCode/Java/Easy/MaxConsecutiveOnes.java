package Easy;

public class MaxConsecutiveOnes {

	public static void main(String[] args){
		
	}
	
	public static int findMaxConsecutiveOnes(int[] nums){
		int max = 0;
		int currMax = 0;
		for (int x : nums){
			if (x == 1){
				currMax++;
				max = Math.max(max, currMax);
			} else {
				currMax = 0;
			}
			
		}
		
		return max;
	}
	
	
	
}
