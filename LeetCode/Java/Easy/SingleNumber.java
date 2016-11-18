package Easy;

import java.util.*;

public class SingleNumber {

	public static void main(String[] args) {
		int[] arr = {4,3,4,3};
		System.out.println(singleNumber(arr));

	}
	
	public static int singleNumber(int[] nums){
		int num = 0;
		for (int i=0; i < nums.length; i++){
			num ^= nums[i];
		}
		
		return num;
	}

}
