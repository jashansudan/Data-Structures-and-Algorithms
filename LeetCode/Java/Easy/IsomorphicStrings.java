package Easy;

import java.util.HashMap;

public class IsomorphicStrings {

	public static void main(String[] args) {

	}
	
	public static boolean isIsomorphic(String s, String t){
		if (s.length() != t.length()){
			return false;
		}
		HashMap<Character,Character> cMap = new HashMap<Character, Character>();
		for (int i =0; i <s.length(); i++){
			char sChar = s.charAt(i);
			char tChar = t.charAt(i);
			
			if (cMap.containsKey(sChar)){
				if(cMap.get(sChar) != tChar){
					return false;
				}
			} else {
				if (cMap.containsValue(tChar)){
					return false;
				}
				cMap.put(sChar, tChar);
			}
		}
		return true;
		
	}

}
