package Easy;

import java.util.*;

public class FizzBuzz {

	public static void main(String[] args) {
		List<String> fbuzz = fizzBuzz(15);
		for(int i =0; i < fbuzz.size(); i++){
			System.out.println(fbuzz.get(i));
		}
	}
	
	public static List<String> fizzBuzz(int n){
		List<String> fbuzz = new ArrayList<String>();
		for(int i = 1; i <= n; i++){
			if ( i % 5 ==0 && i %3 == 0){
				fbuzz.add("FizzBuzz");
			}
			else if (i % 3 == 0){
				fbuzz.add("Fizz");
			}
			else if (i % 5 == 0){
				fbuzz.add("Buzz");
			}
			else {
				fbuzz.add(Integer.toString(i));
			}
			
		}
		
		
		return fbuzz;
	}

}
