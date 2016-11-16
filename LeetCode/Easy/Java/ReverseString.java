package Easy;

public class ReverseString {
	
	public static void main(String [] args){
		String test = reverseString("Hello");
		System.out.println(test);
	}
	
	public static String reverseString(String s){
		char[] charArr = s.toCharArray();
		int start = 0;
		int end = charArr.length -1;
		while(start < end){
			char temp = charArr[start];
			charArr[start] = charArr[end];
			charArr[end] = temp;
			start++;
			end--;
		}
		String  str = new String(charArr);
		return str;
	}

}
