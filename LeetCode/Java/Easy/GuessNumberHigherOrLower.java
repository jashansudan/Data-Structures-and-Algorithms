package Easy;

public class GuessNumberHigherOrLower {

	public void main(String[] args) {

	}

	
	public int guessNumber(int n){
		int low = 1;
		int high = n;
		while (low < high){
			int mid =  low + (high - low)/2;
			if (guess(mid)==0){
				return mid;
			} else if (guess(mid) == 1){
				low = mid + 1;
			} else {
				high = mid;
			}
		}
		return low;
	}

	
	//holder code
	public int guess(int num){
		return num;
	}
}
