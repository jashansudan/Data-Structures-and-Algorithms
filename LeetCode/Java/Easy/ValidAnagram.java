package Easy;

import java.util.*;

public class ValidAnagram {

	public static void main(String[] args) {
		System.out.println(isAnagram("anagram", "nagaram"));

	}
	
	public static boolean isAnagram(String s, String t){
		char[] temp1 = s.toCharArray();
		char[] temp2 = t.toCharArray();
		Arrays.sort(temp1);
		Arrays.sort(temp2);
		s = String.valueOf(temp1);
		t = String.valueOf(temp2);
		if (s.equals(t)){
			return true;
		}
		return false;
	}

}
