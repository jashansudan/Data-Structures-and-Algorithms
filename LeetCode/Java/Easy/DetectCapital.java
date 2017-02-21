package Easy;

public class DetectCapital {
	
	public static void main (String[] args){
		System.out.println(detectCapitalUse("USA"));
	}
	
	public static boolean detectCapitalUse(String word){
		for (int i =0; i < word.length()-1; i++){
			if (Character.isUpperCase(word.charAt(i)) != Character.isUpperCase(word.charAt(i+1))){
				if (i != 0){
					return false;
				} else if (Character.isUpperCase(word.charAt(i+1))){
					return false;
				}
			}
		}
		return true;
	}

}
