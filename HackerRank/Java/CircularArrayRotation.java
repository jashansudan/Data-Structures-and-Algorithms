import java.util.*;

public class CircularArrayRotation {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int size = scan.nextInt();
		int shift = scan.nextInt();
		int queries = scan.nextInt();
		int[] arr = new int[size];
		
		//load up array
		for (int i = 0; i < size; i++){
			arr[i] = scan.nextInt();
		}
		
		//do the shifts
		
		
		
		//
		for (int i = 0; i < queries; i++){
			int index = scan.nextInt();
			System.out.println(arr[index]);
		}
		
		

	}
	
	public static void shift(int[] arr, int shift){
		int len = arr.length;
		
		for (int i = 0; i < shift; i++){
			int count = 0;
			int temp = arr[count];
			while (count != len) {
				arr[count+1%len-1] = temp;
				
				
				count++;
			}
		}
		
		
	}

}
