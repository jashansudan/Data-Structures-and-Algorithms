package Easy;

public class PlusOne {
	
	public void main(String[] args){
		
	}
	
	public int[] plusOne(int[] digits){
		int len = digits.length;
		
		for(int i=len-1; i>=0; i--){
			if(digits[i] < 9){
				digits[i]++;
				return digits;
			}
			digits[i]=0;
		}
		int[] sum = new int[len+1];
		sum[0] = 1;
		
		return sum;
	}

}
