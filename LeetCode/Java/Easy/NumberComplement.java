package Easy;

public class NumberComplement {

	public static void main(String[] args) {
		System.out.println(findComplement(5));
	}

	
	public static int findComplement(int num){
		int complement = 0;
		int mask = 1;
		while (num != 0){
			if ((num & 1) == 0){
				complement = complement | mask;
			} 
			mask = mask << 1;
			num = num >> 1;
		}
		return complement;
	}
}
