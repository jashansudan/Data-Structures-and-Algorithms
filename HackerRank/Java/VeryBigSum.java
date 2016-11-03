import java.util.Scanner;


public class VeryBigSum {

	public static void main(String[] args){
		
		long sum = 0;
        Scanner scan = new Scanner(System.in);
        int total = scan.nextInt();
        for (int i =0; i < total; i++){
        	sum = sum + scan.nextLong();
        }
        System.out.println(sum);
		
	}
	
}
