package Easy;

public class RemoveDuplicatesFromSortedArray {

	public static void main(String[] args) {
		int[] arr = {1,1,2};
		System.out.println(removeDuplicates(arr));
	}
	
	public static int removeDuplicates(int[] nums){
		int i = 0;
		int j = 0;
		
		while (j < nums.length){
			if (nums[j] == nums[i]){
				j++;
			} else {
				i++;
				nums[i] = nums[j];
				j++;
			}
		}
		return i + 1;
	}

}
