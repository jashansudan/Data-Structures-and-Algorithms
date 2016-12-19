package Easy;

public class RepeatedSubstringPattern {

	public static void main(String[] args) {
		

	}
	
	public static boolean repeatedSubstringPattern(String str){
		int len = str.length();
		for (int i = len/2; i>=1; i--){
			if (len % i ==0){
				int m = len/i;
				String subStr = str.substring(0, i);
				int j;
				for (j =1; j < m; j++){
					if (!subStr.equals(str.substring(j*i, j * i + i))){
						break;
					}
				}
				if (j == m){
					return true;
				}
			}
		}
		return false;
	}

}
