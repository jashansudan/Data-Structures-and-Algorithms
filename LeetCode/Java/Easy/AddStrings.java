package Easy;

public class AddStrings {
	
	public static void main(String[] args){
		String str = "Hello";
		System.out.println(str.charAt(-1));
		
		
		
	}
	
	public static String addAtrings(String num1, String num2){
		StringBuilder sum = new StringBuilder();
		int count1 = num1.length() - 1;
		int count2 = num2.length() - 1;
		int carry = 0;
		while (count1 >= 0 || count2 >= 0 || carry == 1){
			int x = 0;
			int y = 0;
			if (count1 > 0){
				x = num1.charAt(count1) - '0';
			}
			if (count2 > 0){
				y = num2.charAt(count2) - '0';
			}
			sum.append((x + y + carry)%10);
			carry =  (x+y+carry)/10;
			count1--;
			count2--;
		}
		return sum.reverse().toString();
	}

}
