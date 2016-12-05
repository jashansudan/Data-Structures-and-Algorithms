package Easy;

public class MinumumMovesToEqualArray {

	public static void main(String[] args) {
		

	}
	
	public static int minMoves(int[] nums){
		int len = nums.length;
		int min = 2147483647;
		int sum = 0;
		for (int x: nums){
			if (x < min){
				min = x;
			}
			sum +=x;
		}
		sum = sum - (min * len);
		return sum;
	}

}
