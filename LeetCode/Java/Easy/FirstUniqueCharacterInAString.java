package Easy;
import java.util.*;

public class FirstUniqueCharacterInAString {

	public static void main(String[] args) {
		
		System.out.println(firstUniqueChar("lleettcoode"));
	}
	
	public static int firstUniqueChar(String s){
		int[] count = new int[26];
		for (int i=0; i<s.length(); i++){
			count[s.charAt(i)- 'a']++;
		}
		for (int j=0; j < s.length(); j++){
			if (count[s.charAt(j) - 'a'] == 1){
				return j;
			}
		}
		
		
		
		return 0;
	}

}
