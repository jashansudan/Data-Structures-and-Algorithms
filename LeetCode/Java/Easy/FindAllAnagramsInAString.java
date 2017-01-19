package Easy;

import java.util.*;

public class FindAllAnagramsInAString {

	public void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public List<Integer> findAnagrams(String s, String p){
		List<Integer> list = new ArrayList();
		if (s == null || s.length() == 0 || p == null || p.length() == 0){
			return list;
		}
		int[] hash = new int[128];
		
		for (char c : p.toCharArray()){
			hash[c]++;
		}
		
		int left = 0;
		int right = 0;
		int count = p.length();
		
		while (right < s.length()){
			if (hash[s.charAt(right++)]-- >= 1){
				count--;
		}
			if (count == 0){
				list.add(left);
			}
			
			if (right - left == p.length() && hash[s.charAt(left++)]++ >= 0){
				count++;
			}
		}
		
		return list;
	}

}
