package Easy;

import java.util.*;

public class ConstructTheRectangle {

	public static void main(String[] args) {
		int[] nums = constructRectangle(12);
		for (int x: nums){
			System.out.println(x);
		}
	}
	
	
	public static int[] constructRectangle(int area){
		int[] dimensions = {area, 1};
		int smallestDifference = area - 1;
		for (int i =2; i <= area/2; i++){
			if (area % i == 0){
				int factor = area / i;
				if (i < factor){
					continue;
				}
				if (i - factor < smallestDifference){
					smallestDifference = i - factor;
					dimensions[0] = i;
					dimensions[1] = factor;
				}
			}
		}
		return dimensions;
	}

}
