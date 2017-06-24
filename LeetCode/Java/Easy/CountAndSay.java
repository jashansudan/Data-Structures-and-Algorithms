package Easy;

public class CountAndSay {
	
	public static void main(String[] args){
		System.out.println(countAndSay(4));
	}
	
	public static String countAndSay(int n){
		String currString = "1";
		
		while (n > 1){
			char prev = currString.charAt(0);
			int count = 1;
			StringBuilder newString = new StringBuilder();
			for (int i = 1; i < currString.length(); i++){
				if (currString.charAt(i) == prev){
					count++;
				}
				else {
					newString.append(count);
					newString.append(prev);
					prev = currString.charAt(i);
					count = 1;
				}
			}
			newString.append(count);
			newString.append(prev);
			currString = newString.toString();
			n--;
		}
		
		return currString;
	}

}
