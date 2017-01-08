package Easy;

public class ReverseVowelsOfAString {
	
	public final static String vowels = "aeiouAEIOU";

	public static void main(String[] args) {
		System.out.println(reverseVowels("hello"));
	}
	
	public static String reverseVowels(String s){
		int first = 0;
		int last = s.length() - 1;
		char[] arr = s.toCharArray();
		while(first < last) {
			while (first < last && vowels.indexOf(arr[first]) == -1){
				first++;
			}
			while (first < last && vowels.indexOf(arr[last]) == -1){
				last--;
			}
			char temp = arr[first];
			arr[first] = arr[last];
			arr[last] = temp;
			first ++;
			last--;
		}
		return new String(arr);
	}

}
