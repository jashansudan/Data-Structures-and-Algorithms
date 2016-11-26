package Easy;

import java.util.*;

public class ContainsDuplicates {
	
	public static void main(String[] args){
		
	}
	
	public static boolean containsDuplicates(int[] nums){
		HashMap<Integer, Integer> numMap = new HashMap<Integer, Integer>();
		for (int i=0;i<nums.length;i++){
			if(numMap.containsKey(nums[i])){
				return true;
			}
			else {
				numMap.put(nums[i], 1);
			}
		}
		return false;
	}

}
