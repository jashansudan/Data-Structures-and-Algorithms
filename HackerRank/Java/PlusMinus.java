import java.util.*;


public class PlusMinus {
	
	public static void main (String[] args){
		Scanner scan = new Scanner(System.in);
		int size = scan.nextInt();
		double total = 0;
		double posCount = 0;
		double negCount = 0;
		double zeroCount = 0;
		for (int i = 0; i < size; i++){
			int temp = scan.nextInt();
			if (temp == 0){
				zeroCount++;
				total++;
			}
			else if (temp < 0){
				negCount++;
				total++;
			}
			else {
				posCount++;
				total++;
			}
		}
		System.out.printf("%.6f%n", posCount/total);
		System.out.printf("%.6f%n", negCount/total);
		System.out.printf("%.6f%n", zeroCount/total);
		
		
	}

}
