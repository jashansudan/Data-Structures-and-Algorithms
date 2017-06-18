package Easy;

import java.util.HashSet;

public class DistributeCandies {
	
	public static void main(String[] args){
		
	}
	
	public int distributeCandies(int[] candies){
		
		HashSet<Integer> candiesSet = new HashSet();
		
		for (int x: candies){
			candiesSet.add(x);
		}
		return Math.min(candies.length/2, candiesSet.size());
	}

}
