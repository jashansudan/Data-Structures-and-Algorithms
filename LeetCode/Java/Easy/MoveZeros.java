package Easy;

public class MoveZeros {

	public static void main(String[] args) {
		int[] test = {0, 1, 0, 3, 12};
		moveZeros(test);
		for(int i=0; i<test.length;i++){
			System.out.println(test[i]);
		}

	}
	
	public static void moveZeros(int[] nums){
		if (nums.length < 2){
			return;
		}
		int ptr1 = 0;
		int ptr2 = 1;
		while (ptr1 < nums.length && ptr2 < nums.length){
			if(nums[ptr1] == 0 && nums[ptr2] != 0){
				int temp = nums[ptr1];
				nums[ptr1] = nums[ptr2];
				nums[ptr2] = temp;
				ptr1++;
				ptr2++;
			}
			else if (nums[ptr1] == 0){
				ptr2++;
			}
			else {
				ptr1++;
				ptr2++;
			}
		}
		return;
	}

}
