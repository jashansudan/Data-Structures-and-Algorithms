package Easy;

import java.util.*;
public class RansomNote {

	public static void main(String[] args) {
		
		boolean test =canConstruct("aa", "aab");
		System.out.println(test);
		
	}
	
	
	public static boolean canConstruct(String ransomNote, String magazine){
		
		char[] ransomArr = ransomNote.toCharArray();
		char[] magazineArr = magazine.toCharArray();
		HashMap<Character, Integer> magMap = new HashMap<Character, Integer>();
		for (int i = 0; i < magazineArr.length; i++){
			if (magMap.containsKey(magazineArr[i])){
				magMap.put(magazineArr[i], magMap.get(magazineArr[i]) + 1);
			}
			else {
				magMap.put(magazineArr[i], 1);
			}
		}
		
		for (int j = 0; j< ransomArr.length; j++){
			if (!magMap.containsKey(ransomArr[j]) ){
				return false;
			}
			else if (magMap.get(ransomArr[j]) == 0){
				return false;
			}
			else {
				magMap.put(ransomArr[j], magMap.get(ransomArr[j])-1);
			}
		}
		return true;
	}

}
