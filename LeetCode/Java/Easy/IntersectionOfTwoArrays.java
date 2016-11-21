package Easy;

import java.util.*;

public class IntersectionOfTwoArrays {
	
	public static void main (String[] args){
		int[] nums1 = {1,2,2,1};
		int[] nums2 = {2,2};
		int[] intersection = intersection(nums1, nums2);
		for (int i =0; i < intersection.length; i++){
			System.out.println(intersection[i]);
		}
	}
	
	public static int[] intersection(int[] nums1, int[] nums2){
		Arrays.sort(nums1);
		Arrays.sort(nums2);
		ArrayList<Integer> arrList = new ArrayList<Integer>();
		int start1 = 0;
		int start2 = 0;
		int curr = 0;
		while (start1 < nums1.length && start2 < nums2.length){
			if (nums1[start1] == nums2[start2]){
				if (curr>0){
					if (nums1[start1] == arrList.get(curr-1)){
						start1++;
						start2++;
						continue;
					}
				}
				arrList.add(nums1[start1]);
				curr++;
			}
			else if (nums1[start1] >= nums2[start2]){
				start2++;
			}
			else{
				start1++;
			}
		}
		int[] intersection = new int[curr];
		for (int i =0; i <curr; i++){
			intersection[i] = arrList.get(i);
		}
		return intersection;
		
	}

}
