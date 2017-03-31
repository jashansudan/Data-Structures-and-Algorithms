package Easy;

public class ReverseStringTwo {
	
	public static void main(String[] args){
		System.out.println(reverseStr("abcdefg", 2));
	}
	
	public static String reverseStr(String s, int k){
		char[] charArr = s.toCharArray();
		boolean reverse = false;
		for (int i = 0; i < charArr.length; i = i +k){
			if (reverse == false){
				reverse = true;
			} else {
				reverse = false;
			}
			if (reverse){
				reverse(charArr, k, i);
			}
		}
		return new String(charArr);
	}
	
	public static void reverse(char[] arr, int k, int index){
		int end = index + k-1;
		if (end > arr.length-1){
			end = arr.length-1;
		}
		while (index < end){
			char temp = arr[end];
			arr[end] = arr[index];
			arr[index] = temp;
			index++;
			end--;
		}
	}
}
