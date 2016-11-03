
public class CountingChange {
	
	public static void main(String[] args){
		int[] coins = {41,34,46,9,37,32,42,21,7,13,1,24,3,43,2,24,8,45,19,30,29,18,35,11};
		countChange(coins, 250);
	}
	
	public static void countChange(int[] coins, int goal){
		
		long[] val = new long[goal+1];
		val[0] = 1;
		
		for (int coin: coins){
			for (int i = coin; i <= goal; i++){
				if (i - coin >= 0){
					val[i] += val[i-coin];
				}
				
			}
		}
		System.out.println(val[goal]);
		
	}

}
