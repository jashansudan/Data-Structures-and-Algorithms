package Easy;

public class ValidPerfectSquare {

	public void main(String[] args){
		
	}
	
	
	public boolean isPerfectSquare(int num){
		long low = 1;
		long high = (long) num;
		while (low <= high){
			long mid = (low + high)/2;
			long midSquared = mid * mid;
			if (midSquared == num){
				return true;
			} else if (midSquared > num){
				high = mid - 1;
			} else {
				low = mid + 1;
			}
		}
		return false;
	}
	
}
