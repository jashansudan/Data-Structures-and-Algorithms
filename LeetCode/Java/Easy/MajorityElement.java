package Easy;

import java.util.*;

public class MajorityElement {
	public static void main(String[] args){
		
	}
	
	public static int majorityElement(int[] nums) {
        HashMap<Integer, Integer> numMap = new HashMap<Integer, Integer>();
		int count = 0;
		int maj= 0;
		for (int i =0; i < nums.length; i++){
			if (numMap.containsKey(nums[i])){
				numMap.put(nums[i], numMap.get(nums[i])+1);
			}
			else{
				numMap.put(nums[i],1);
			}
			if (numMap.get(nums[i]) > count){
				maj = nums[i];
				count = numMap.get(maj);
			}
		}
		return maj;
    }
}
