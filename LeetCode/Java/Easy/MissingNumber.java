package Easy;

public class MissingNumber {

	public static void main(String[] args) {
		int[] arr = {0,1,3,4};
		System.out.println(missingNumber(arr));
	}
	
	
	public static int missingNumber(int[] nums){
		int sumNumbs = (nums.length * (nums.length + 1))/2;
		for (int x : nums){
			sumNumbs-=x;
		}
		return sumNumbs;
	}

}
