package Easy;

public class ArrangingCoins {

	public static void main(String[] args) {
		System.out.println(arrangeCoins(5));
	}
	
	public static int arrangeCoins(int n){
		int i = 0;
		
		while (i < n ){
			n -= i;
			i++;
		}
		return i-1;
	}

}
