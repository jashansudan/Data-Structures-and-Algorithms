import java.util.Scanner;


public class Kangaroo {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		int loc1,speed1,loc2,speed2;
		loc1 = scan.nextInt();
		speed1 = scan.nextInt();
		loc2 = scan.nextInt();
		speed2 = scan.nextInt();
		
		boolean check = tooFast(loc1, speed1, loc2, speed2);
		if (!check){
			System.out.println("NO");
			return;
		}
		
		check = speed(loc1, speed1, loc2, speed2);
		if (!check){
			System.out.println("NO");
			return;
		}
		
		
		
		System.out.println("YES");
	}
	
	//check if one kangaroo is faster and ahead
	public static boolean tooFast(int loc1, int speed1, int loc2, int speed2){
		if (loc1 > loc2 && speed1 > speed2 || loc2 > loc1 && speed2 > speed1){
			return false;
		}
		
		return true;
	}
	
	
	// check if they will land on same area
	public static boolean speed(int loc1, int speed1, int loc2, int speed2){
		int locDiff = Math.abs(loc2 - loc1);
		int speedDiff = Math.abs(speed2 - speed1);
		if (speedDiff == 0){
			return false;
		}
		if (locDiff % speedDiff != 0){
			return false;
		}
		
		
		return true;
	}

}
