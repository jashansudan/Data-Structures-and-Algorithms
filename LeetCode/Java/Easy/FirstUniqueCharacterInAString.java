package Easy;
import java.util.*;

public class FirstUniqueCharacterInAString {

	public static void main(String[] args) {
		
		System.out.println(firstUniqueChar("car"));
	}
	
	public static int firstUniqueChar(String s){
		int[] count = new int[26];
		for (int i=0; i<s.length(); i++){
			char temp = s.charAt(i);
			count[Character.getNumericValue(temp)- Character.getNumericValue('a')]++;
		}
		for (int j=0; j < s.length(); j++){
			char temp = s.charAt(j);
			if (count[Character.getNumericValue(temp)- Character.getNumericValue('a')] == 1){
				return j;
			}
		}
		
		
		return 0;
	}

}
