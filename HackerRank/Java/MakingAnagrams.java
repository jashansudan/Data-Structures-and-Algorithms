import java.util.*;

public class MakingAnagrams {
	
	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String a = in.next();
        String b = in.next();
     
        System.out.println(makeAnagram(a,b));
        
    }
	
	public static int makeAnagram(String str1, String str2){
		char[] charArr1 = str1.toCharArray();
		char[] charArr2 = str2.toCharArray();
		Arrays.sort(charArr1);
		Arrays.sort(charArr2);
		
		return countDiffs(charArr1, charArr2);
	}
	
	public static int countDiffs(char[] charArr1, char[] charArr2){
		int count = 0;
		int i = 0;
		int j = 0;
		while (i < charArr1.length && j < charArr2.length){
			if (charArr1[i] == charArr2[j]){
				i++;
				j++;
			}
			else if (charArr1[i] > charArr2[j]){
				count++;
				j++;
			}
			else {
				count++;
				i++;
			}
		}
		count = count + charArr1.length + charArr2.length - i - j;
		
		return count;
	}

}
