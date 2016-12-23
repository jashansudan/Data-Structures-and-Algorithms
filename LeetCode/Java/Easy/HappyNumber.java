package Easy;
import java.util.*;

public class HappyNumber {

	public static void main(String[] args){
		
	}
	
	public static boolean isHappy(int n){
		HashSet<Integer> numSet = new HashSet<Integer>();
		
		while (!numSet.contains(n)){
			numSet.add(n);
			n = getSum(n);
			if (n == 1){
				return true;
			}
		}
			
		return false;
	}
	
	public static int getSum (int n){
		int sum = 0;
		while (n > 0){
			sum += (n % 10) * (n % 10);
			n = n/10;
		}
		return sum;
	}

}
