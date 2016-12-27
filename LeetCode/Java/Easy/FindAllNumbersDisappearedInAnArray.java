package Easy;

import java.util.*;

public class FindAllNumbersDisappearedInAnArray {
	
	public static void main(String[] args){
		
	}
	
	public static List<Integer> findDissapeared(int[] nums){
		List<Integer> missing = new ArrayList<Integer>();
		
		// Mark the indices of the numbers seen in the array negative
		// If a double is seen, keep it negative
		for (int i = 0; i < nums.length; i++){
			int val = Math.abs(nums[i]) - 1;
			if (nums[val] > 0){
				nums[val] = -nums[val];
			}
		}
		
		// Go through the array and if a positive index is found, it means the corresponding number is not in the array
		for (int i =0; i < nums.length; i++){
			if(nums[i] > 0){
				missing.add(i+1);
			}
		}
		
		return missing;
	}

}
