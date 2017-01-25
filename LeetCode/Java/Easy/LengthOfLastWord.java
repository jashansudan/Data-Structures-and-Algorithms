package Easy;

public class LengthOfLastWord {

	public void main(String[] args) {
		
		System.out.println(lengthOfLastWord("Hello World"));
	}
	
	public int lengthOfLastWord(String s){
		int last = 0;
		char prev = ' ';
		int len = s.length();
		
		for (int i = 0; i < len; i++){
			if (Character.isLetter(s.charAt(i))){
				if (!Character.isLetter(prev)){
					last = 1;
				} else {
					last++;
				}
			}
			prev = s.charAt(i);
		}
		
		return last;
	}

}
