package Easy;

public class LongestUncommonSubsequenceOne {
	
	public static void main(String[] args){
		
		
	}
	
	public int findLUSlength(String a, String b){
		return a.equals(b) ? -1 : Math.max(a.length(), b.length());
	}

}
