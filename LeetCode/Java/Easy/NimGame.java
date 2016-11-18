package Easy;

import java.util.*;
public class NimGame {
	
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		int stones = scan.nextInt();
		nimGame(stones);
	}
	
	public static boolean nimGame(int stones){
		if (stones % 4 != 0){
			return true;
		}
		return false;
	}

}
