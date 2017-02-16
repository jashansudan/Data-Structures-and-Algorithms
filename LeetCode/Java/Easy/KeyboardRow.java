package Easy;

import java.util.*;

public class KeyboardRow {
	
	public static void main(String[] args){
		
	}
	

	
	public String[] findWord(String[] words){
		HashMap<Character, Integer> keyMap = new HashMap<>();
		String[] keyboard = {"QWERTYUIOP","ASDFGHJKL","ZXCVBNM"};
		for (int i = 0; i < keyboard.length; i++){
			for (char c : keyboard[i].toCharArray()){
				keyMap.put(c, i);
			}
		}
		
		ArrayList<String> approvedWords = new ArrayList<>();
		for (int j = 0; j < words.length; j++){
			int index = keyMap.get(words[j].toUpperCase().charAt(0));
			for (char c : words[j].toUpperCase().toCharArray()){
				if (keyMap.get(c) != index){
					index = -1;
					break;
				}
			}
			if (index != -1){
				approvedWords.add(words[j]);
			}
		}
		String[] wordsList = new String[approvedWords.size()];
		wordsList = approvedWords.toArray(wordsList);
		return wordsList;
		
	}
	

}
