import java.util.*;

public class RansomNote {
	
	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int m = in.nextInt();
        int n = in.nextInt();
        String magazine[] = new String[m];
        for(int magazine_i=0; magazine_i < m; magazine_i++){
            magazine[magazine_i] = in.next();
        }
        String ransom[] = new String[n];
        for(int ransom_i=0; ransom_i < n; ransom_i++){
            ransom[ransom_i] = in.next();
        }
        
        System.out.println(checkWords(magazine, ransom));
    }
	
	public static String checkWords(String[] magazine, String[] ransom){
		HashMap<String, Integer> magazineMap = new HashMap<String, Integer>();
		for (int i =0; i <magazine.length; i++){
			if (magazineMap.containsKey(magazine[i])){
				magazineMap.put(magazine[i], magazineMap.get(magazine[i]) + 1);
			}
			else {
			magazineMap.put(magazine[i], 1);
			}
		}
		
		
		for (int i = 0; i <ransom.length; i ++){
			if (magazineMap.containsKey(ransom[i])){
				if (magazineMap.get(ransom[i]) > 0){
					magazineMap.put(ransom[i], magazineMap.get(ransom[i]) - 1);
				}
				else {
					return "No";
				}
			}
			else {
				return "No";
			}
		}
		
		return "Yes";
	}

}
