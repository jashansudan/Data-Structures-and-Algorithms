package Easy;

public class ReverseWordsInAStringThree {
	
	public static void main(String[] args){
		
		System.out.println(reverseWords("s'teL ekat edoCteeL tsetnoc"));
	}
	
	public static String reverseWords(String s){
		StringBuilder reversed = new StringBuilder();
		String[] stringsArr = s.split(" ");
		for (int i = 0; i < stringsArr.length-1; i++){
			reversed.append(reverse(stringsArr[i]));
			reversed.append(" ");
		}
		reversed.append(reverse(stringsArr[stringsArr.length-1]));
		return reversed.toString();
	}
	
	
	public static String reverse(String s){
		StringBuilder newString = new StringBuilder();
		for (int i = s.length()-1; i >= 0; i--){
			newString.append(s.charAt(i));
		}
		return newString.toString();
	}

}
