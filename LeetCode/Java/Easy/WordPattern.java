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
		HashMap map = new HashMap();
		
		for (Integer i = 0; i < sArr.length; i++){
			if (map.put(pattern.charAt(i), i) != map.put(sArr[i], i)){
				return false;
			}
		}
		
		return true;
	}
}


