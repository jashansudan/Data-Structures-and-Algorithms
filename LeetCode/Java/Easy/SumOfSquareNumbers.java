package Easy;

import java.util.*;

public class SumOfSquareNumbers {
	public static void main(String[] args){
		
	}
	
	public boolean judgeSquareSum(int c){
		int low = 0;
		int high = (int) Math.sqrt(c);
		
		while (low <= high){
			int squaredSum = low * low + high * high;
			if (squaredSum == c) return true;
			if (squaredSum > c){
				high--;
			}else{
				low++;
			}
		}
		return false;
	}
}
