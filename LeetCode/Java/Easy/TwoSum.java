package Easy;

import java.util.*;

public class TwoSum {
	
	public static void main (String[] args){
		
		int target = 9;
		int[] nums = {2, 7, 11, 15};
		int[] arr = twoSum(nums, target);
		for (int i = 0; i < arr.length; i++){
			System.out.println(arr[i]);
		}
		
		
	}
	
	public static int[] twoSum (int[] nums, int target) {
		HashMap<Integer, Integer> numMap = new HashMap<Integer, Integer>();
		int[] soln = {-1,-1};
		for (int i = 0; i< nums.length; i++){
			if (numMap.containsKey(target - nums[i])){
				soln[0] = numMap.get(target - nums[i]);
				soln[1] = i;
				return soln;
			}
			else {
				numMap.put(nums[i], i);
			}
		}
		return soln;
	}

}
