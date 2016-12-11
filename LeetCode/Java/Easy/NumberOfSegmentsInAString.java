package Easy;

public class NumberOfSegmentsInAString {
	
	public static void main(String[] args){
		System.out.println(countSegments("Hello, my name is John"));
	}
	
	public static int countSegments(String s){
		int len = s.length();
		int count = 0;
		char prev = ' ';
		char curr = ' ';
		for (int i = 0; i < len; i++){
			curr = s.charAt(i);
			if(prev == ' ' && curr != ' '){
				count++;
			}
			prev = curr;
		}
		return count;
	}

}
