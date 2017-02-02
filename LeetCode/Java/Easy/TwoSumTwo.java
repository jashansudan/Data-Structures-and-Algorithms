package Easy;

public class TwoSumTwo {

	public static void main(String[] args) {

	}
	
	public int[] twoSum(int[] numbers, int target){
		int ptr1 = 0;
		int ptr2 = numbers.length -1;
		int[] indices = new int[2];
		
		while (ptr1 < ptr2){
			int sum = numbers[ptr1] + numbers[ptr2];
			if ( sum == target){
				indices[0] = ptr1 + 1;
				indices[1] = ptr2 + 1;
				return indices;
			} else if ( sum < target){
				ptr1++;
			} else {
				ptr2--;
			}
		}
		return indices;
	}

}
