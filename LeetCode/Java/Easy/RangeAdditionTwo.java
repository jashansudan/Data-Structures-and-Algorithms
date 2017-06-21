package Easy;

public class RangeAdditionTwo {

	public static void main(String[] args){
		
	}
	
	public int maxCount(int m, int n, int[][] ops){
		if (ops.length == 0){
			return m * n;
		}
		int minRow = ops[0][0];
		int minCol = ops[0][1];
		for (int i =0; i <ops.length; i++){
			minRow = Math.min(minRow, ops[i][0]);
			minCol = Math.min(minCol, ops[i][1]);
		}
		return minRow * minCol;
	}
	
}
