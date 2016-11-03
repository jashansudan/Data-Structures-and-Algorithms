import java.util.*;
public class LeftRotation {
	
	
	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        shift(n,k,a);
        
    }
	
	public static void shift(int len, int shift, int[] arr){
		while (shift > 0){
			int temp1 = arr[len-1];
			int temp2 = arr[len-2];
			for (int i = len-2; i > 0; i--){
				arr[i] = temp1;
				temp1 = temp2;
				temp2 = arr[i-1];
			}
			arr[0] = temp1;
			arr[len-1] = temp2;
			shift--;
		}
		for (int j = 0; j < len; j++){
			System.out.print(arr[j]+ " ");
		}
	}

}
