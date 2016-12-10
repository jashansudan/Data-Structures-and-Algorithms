package Easy;

public class MergeSortedArray {

	public static void main(String[] args){
		
	}
	
	public static void merge(int[] nums1, int m, int[] nums2, int n){
		int len = nums1.length-1;
		while (m > 0 && n > 0){
			if (nums1[m-1] >= nums2[n-1]){
				nums1[len] = nums1[m-1];
				m--;
			}
			else{
				nums1[len] = nums2[n-1];
				n--;
			}
			len--;
		}
		while (n > 0){
			nums1[len] = nums2[n-1];
			len--;
			n--;
		}
	}
}
