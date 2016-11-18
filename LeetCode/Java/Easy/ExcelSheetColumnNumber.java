package Easy;

import java.util.*;

public class ExcelSheetColumnNumber {
	
	public static void main(String[] args){
		System.out.println(titleToNumber("BA"));
	}
	
	public static int titleToNumber(String s){
		int num =0;
		char[] charArr = s.toCharArray();
		int len = charArr.length;
		
		for (int i =0; i < charArr.length; i++){
			if (len > 1){
				num = (int) (num +  (Math.pow(26, len-1) *(Character.getNumericValue(charArr[i]) -9 )));
				len--;		
			}else {
				num = num + (Character.getNumericValue(charArr[i]) -9 );
			}
			
		}

		return num;
	}

}
