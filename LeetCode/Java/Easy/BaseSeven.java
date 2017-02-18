package Easy;

public class BaseSeven {

	public static void main(String[] args) {
		System.out.println(convertToBase7(100));
	}
	
	public static String convertToBase7(int num){
		StringBuilder str = new StringBuilder();
		boolean neg = false;
		if (num < 0){
			neg = true;
		}
		if (num ==0){
			return "0";
		}
		while (num != 0){
			str.append(Math.abs(num%7));
			num /=7;
		}
		if (neg){
			return '-' + str.reverse().toString();
		}
		return str.reverse().toString();
	}

}
