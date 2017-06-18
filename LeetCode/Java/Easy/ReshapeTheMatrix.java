package Easy;

public class ReshapeTheMatrix {
	
	public static void main(String[] args){
		
		
	}
	
	public int[][] matrixReshape(int[][] nums, int r, int c){
		if (nums.length * nums[0].length != r*c){
			return nums;
		}
		
		int[][] reshapedMatrix = new int[r][c];
		int currentRow = 0;
		int currentColumn = 0;
		for (int i =0; i < nums.length; i++){
			for (int j=0; j < nums[0].length; j++){
				reshapedMatrix[currentRow][currentColumn] = nums[i][j];
				currentColumn++;
				if (currentColumn >= c){
					currentColumn = 0;
					currentRow++;
				}
			}
		}
		return reshapedMatrix;
	}

}
