package Easy;

import java.util.*;

public class NextGreaterElementOne {

	public static void main(String[] args) {

	}
	
	
	public int[] nextGreaterElement(int[] findNums, int[] nums){
		HashMap<Integer, Integer> map = new HashMap<>();
		Stack<Integer> stk = new Stack<>();
		for (int num : nums){
			while (!stk.empty() && stk.peek() < num){
				map.put(stk.pop(), num);
			}
			stk.push(num);
		}
		for (int i=0; i<findNums.length;i++){
			findNums[i] = map.getOrDefault(findNums[i], -1);
		}
		return findNums;
	}

}
