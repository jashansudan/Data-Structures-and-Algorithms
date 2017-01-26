package Easy;

import java.util.*;

public class WordPattern {

	public void main(String[] args) {
	}
	
	public boolean wordPattern(String pattern, String str){
		String[] sArr = str.split(" ");
		if (sArr.length != pattern.length()){
			return false;
		}
		HashMap<Character, String> map = new HashMap<Character, String>();
		for (int i = 0;i < sArr.length; i++){
			char c = pattern.charAt(i);
			if (map.containsKey(c)){
				if(!map.get(c).equals(sArr[i])){
					return false;
				} 
			} else {
				if (map.containsValue(sArr[i])){
					return false;
				}
				map.put(c, sArr[i]);
			}
		}
		
		return true;
	}
}
