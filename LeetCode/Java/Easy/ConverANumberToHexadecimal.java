package Easy;

public class ConverANumberToHexadecimal {
	public static void main(String[] args){
		System.out.println(toHex(15));
	}
	
	public static String toHex(int num){
		StringBuilder hex = new StringBuilder();
		char[] hexMap = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'};
		if (num == 0){
			return "0";
		}
		while (num != 0){
			hex.append(hexMap[num & 15]);
			num = num >>> 4;
		}
		
		return hex.reverse().toString();
	}
	
}
