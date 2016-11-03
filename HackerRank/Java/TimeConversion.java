import java.util.*;

public class TimeConversion {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		String oT = scan.next();
		int hourOrig = Integer.parseInt(oT.substring(0, 2));

		String sun = oT.substring(8, 10);
		
		
		if ( sun.equals("PM")){
				if (hourOrig == 12){
				
					oT = "12" + oT.substring(2, 8);
					System.out.println(oT);
				}
			
			else {
				int hour = hourOrig + 12;
			
				oT = Integer.toString(hour) + oT.substring(2, 8);
				System.out.println(oT);
			}
			
		}
		else {
			if (hourOrig == 12){
				
				oT = "00" + oT.substring(2, 8);
				System.out.println(oT);
			}
			else {
			System.out.println(oT.substring(0,8));
			}
		}
		

	}

}
