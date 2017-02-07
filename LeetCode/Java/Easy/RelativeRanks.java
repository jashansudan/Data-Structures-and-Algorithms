package Easy;

import java.util.Arrays;
import java.util.Collections;

public class RelativeRanks {

	public static void main(String[] args) {
		int[] arr = {5,4,3,2,1};
		String[] arr2 = findRelativeRanks(arr);
		for (String y: arr2){
			System.out.println(y);
		}
	}
	
	public static String[] findRelativeRanks (int[] nums){
		int[] copy = Arrays.copyOf(nums, nums.length);
		Arrays.sort(copy);
		String[] ranked = new String[nums.length];
		for (int i = 0; i < nums.length; i++){
			int pos = nums.length - 1 - binSearch(nums[i], copy);
			if (pos == 0){
				ranked[i] = "Gold Medal";
			} else if (pos == 1){
				ranked[i] = "Silver Medal";
			} else if (pos == 2){
				ranked[i] = "Bronze Medal";
			} else {
				ranked[i] = Integer.toString(pos + 1);
			}
		}
		return ranked;
	}
	
	public static int binSearch(int num, int[] arr){
		int low = 0;
		int high = arr.length-1;
		while (low < high){
			int mid = (low + high)/2;
			if (num == arr[mid]){
				return mid;
			}
			else if (arr[mid] > num){
				high = mid -1;
			} else {
				low = mid + 1;;
			}
		}
		return low;
	}

}
