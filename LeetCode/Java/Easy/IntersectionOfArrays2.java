package Easy;

import java.util.*;

public class IntersectionOfArrays2 {

	public static void main(String[] args) {
		

	}
	
	public static int[] intersect(int[] nums1, int[] nums2) {
		ArrayList<Integer> numList = new ArrayList<Integer>();
		Arrays.sort(nums1);
		Arrays.sort(nums2);
		int count1 = 0;
		int count2=0;
		while (count1 < nums1.length && count2 < nums2.length){
			if (nums1[count1] == nums2[count2]){
				numList.add(nums1[count1]);
				count1++;
				count2++;
			}
			else if (nums1[count1] > nums2[count2]){
				count2++;
			}
			else{
				count1++;
			}
		}
		int[] intersection = new int[numList.size()];
		for (int i =0; i < numList.size(); i++){
			intersection[i] = numList.get(i);
		}
		return intersection;
    }

}
