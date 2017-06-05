package Easy;

public class StudentAttendanceRecordI {

	public static void main(String[] args){
		
	}
	
	public static boolean checkRecord(String s){
		int latesInARow = 0;
		int totalTimesAbsent = 0;
		for (int i=0; i <s.length(); i++){
			if (s.charAt(i) == 'P'){
				latesInARow = 0;
			} else {
				if (s.charAt(i) == 'L'){
					latesInARow++;
				}
				else {
					totalTimesAbsent++;
					latesInARow = 0;
				}
				if (totalTimesAbsent >= 2 || latesInARow >= 3){
					return false;
				}
			}
		}
		return true;
	}
}
