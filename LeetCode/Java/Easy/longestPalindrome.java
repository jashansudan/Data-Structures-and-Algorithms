package Easy;

public class longestPalindrome {

	public static void main(String[] args) {
		System.out.println(longestPalindrome("abcccccdd"));
		
	}
	
	
	public static int longestPalindrome(String s){
		int[] count =new int['z' - 'A'+1];
		int max = 0;
		boolean flag = false;
		for(int i=0; i<s.length();i++){
			char c = s.charAt(i);
			count[c - 'A']++;
		}
		for (int x: count){
			if (x > 1){
				max = max + (x/2)*2;
			}
			if (!flag){
				if (x%2 == 1){
					flag = true;
				}
			}
		}
		if (flag){
			max++;
		}
		return max;
	}

}
