package Easy;

public class PowerOfThree {

	public static void main(String[] args) {

	}
	
	public static boolean isPowerOfThree(int n){
		if (n == 0){
			return false;
		}
		if (n == 1){
			return true;
		}
		return n%3==0 && isPowerOfThree(n/3);
	}

}
