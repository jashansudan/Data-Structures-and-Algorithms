package Easy;

import java.util.*;

public class NumberOfBoomerangs {

	public static void main(String[] args) {
	
		

	}
	
	
	public static int numberOfBoomerangs(int[][] points){
		int boomerangs = 0;
		HashMap<Integer, Integer> bMap = new HashMap<>();
		for (int i = 0; i<points.length; i++){
			for (int j =0; j<points.length; j++){
				if (i == j){
					continue;
				}
				int dist = getDistance(points[i], points[j]);
				bMap.put(dist, bMap.getOrDefault(dist, 0) +1);
			}
			for (int val : bMap.values()){
				boomerangs += val * (val-1);
			}
			map.clear();
		}	
		return boomerangs;
	}
	
	public static int getDistance (int[] a, int[] b){
		int dx = a[0] - b[0];
		int dy = a[1] - b[1];
		return dx*dx + dy*dy;
	}

}
