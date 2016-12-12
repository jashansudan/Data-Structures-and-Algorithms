package Easy;

public class RomanToInteger {
	
	public static void main(String[] args){
		
	}
	
	public static int romanToInt(String s){
		int num = 0;
		int len = s.length()-1;
		int prev = 0;
		int current = 0;
		for (int i = len; i >= 0; i--){
			char temp = s.charAt(i);
			if (temp == 'I'){
				current = 1;
			} 
			else if (temp == 'V'){
				current = 5;
			} 
			else if (temp == 'X'){
				current = 10;
			} 
			else if (temp == 'L'){
				current = 50;
			}
			else if (temp == 'C'){
				current = 100;
			}
			else if (temp == 'D'){
				current = 500;
			}
			else {
				current = 1000;
			}
			if (current < prev){
				num -= current;
			} 
			else {
				num += current;
			}
			prev = current;
		}
		
		return num;
	}

}
