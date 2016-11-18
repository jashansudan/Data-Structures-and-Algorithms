package Easy;

import java.util.*;
public class FindTheDifference {

	public static void main(String[] args) {

	}
	
	public char findTheDifference(String s, String t){
		char[] charArray1 = s.toCharArray();
		char[] charArray2 = t.toCharArray();
		Arrays.sort(charArray1);
		Arrays.sort(charArray2);
		for (int i =0; i < charArray1.length; i++){
			if (charArray1[i] != charArray2[i]){
				return charArray2[i];
			}
		}
		return charArray2[charArray1.length];
	}

}
