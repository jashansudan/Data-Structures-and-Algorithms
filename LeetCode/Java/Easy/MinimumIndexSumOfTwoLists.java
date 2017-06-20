package Easy;

import java.util.*;

public class MinimumIndexSumOfTwoLists {
	
	public static void main(String[] args){
		
		
	}
	
	public String[] findRestauraunt(String[] list1, String[] list2){
		
		HashMap<String, Integer> indexMap = new HashMap();
		for (int i = 0; i < list1.length; i++){
			indexMap.put(list1[i], i);
		}
		
		ArrayList<String> minList = new ArrayList();
		int minIndex = Integer.MAX_VALUE;
		for (int j = 0; j < list2.length; j++){
			Integer index = indexMap.get(list2[j]);
			if (index != null && index + j <= minIndex){
				if (index + j < minIndex){
					minList.clear();
					minIndex = index + j;
				}
				minList.add(list2[j]);
			}
		}
		
		return minList.toArray(new String[minList.size()]);
	}
}
