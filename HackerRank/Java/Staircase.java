import java.util.*;

public class Staircase {
	
	public static void main(String[] args){
		
		Scanner scan = new Scanner(System.in);
		int size = scan.nextInt();
		int sizeDec = size - 1;
		int sizeInc = 1;
		
		for (int i =0; i < size; i++){
			for (int j = 0; j < sizeDec; j++){
				System.out.print(" ");
				
			}
			for (int k = 0; k < sizeInc; k++){
				System.out.print("#");
			}
			sizeDec--;
			sizeInc++;
			System.out.println();
		}
		
		
		
	}

}
