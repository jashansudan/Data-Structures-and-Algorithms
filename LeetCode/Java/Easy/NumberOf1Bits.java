package Easy;

public class NumberOf1Bits {

	public static void main(String[] args){
		System.out.println(hammingWeight(2147483648));
	}
	
	public static int hammingWeight(int n){
		int bits = 0;
		while (n!=0){
			if ((1 & n) == 1){
				bits++;
			}
			n = n >> 1;
		}
		return bits;
	}
	
}
