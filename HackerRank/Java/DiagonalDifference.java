import java.util.Scanner;


public class DiagonalDifference {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int d2Count = n;
		int d1Count = 1;
		int d1Sum = 0;
		int d2Sum = 0;
		
		for (int i = 1; i <= n; i++){
			for (int j = 1; j <= n; j++){
				int temp = scan.nextInt();
				if (j == d1Count){
					d1Sum = d1Sum + temp;
				}
				if (j == d2Count){
					d2Sum = d2Sum + temp;
				}
			}
			d2Count--;
			d1Count++;
		}
		
		int diff = Math.abs(d1Sum - d2Sum);
		System.out.println(diff);
		

	}
	
	

}
