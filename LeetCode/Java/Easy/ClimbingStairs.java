package Easy;

public class ClimbingStairs {

	public static void main(String[] args) {
		System.out.println(climbStairs(2));

	}
	
	public static int climbStairs(int n){
		int[] stairs = new int[n+1];
		stairs[0] = 1;
		if (n > 0){
			stairs[1] = 1;
		}
		int stair = 2;
		while (stair < n+1){
			stairs[stair] = stairs[stair-1] + stairs[stair-2];
			stair++;
		}
		return stairs[n];
	}

}
