import java.util.Scanner;


public class SimpleArraySum {

	public static void main(String[] args){
		
		Scanner readIn = new Scanner(System.in);
		int size = readIn.nextInt();
		int sum = 0;
		
		for (int i =0; i < size; i++){
			sum += readIn.nextInt();
		}
		
		System.out.println(sum);
		readIn.close();
		
	}
}
