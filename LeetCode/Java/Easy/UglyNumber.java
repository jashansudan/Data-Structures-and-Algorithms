package Easy;

public class UglyNumber {

	public static void main(String[] args) {
		
		System.out.println(isUgly(14));
	}
	
	public static boolean isUgly(int num){
		
		int prev = num;
		while (num != 1){
			if (num % 2 == 0){
				num = num/2;
			}
			if (num % 5 == 0){
				num = num/5;
			}
			if (num % 3 == 0){
				num = num/3;
			}
			if (prev == num){
				return false;
			}
			prev = num;
		}
		
		return true;
	}

}
