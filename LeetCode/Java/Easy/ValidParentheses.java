package Easy;

import java.util.*;

public class ValidParentheses {

	public static void main(String[] args) {

	}
	
	public boolean isValid(String s){
		Stack<Character> parenStk = new Stack<Character>();
		int len = s.length();
		for (int i = 0; i < len; i++){
			if (s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{'){
				parenStk.push(s.charAt(i));
			} else {
				if (parenStk.isEmpty()){
					return false;
				}
				if (s.charAt(i) == ')' && '(' != parenStk.peek()){
					return false;
				} else if (s.charAt(i) == ']' && '[' != parenStk.peek()){
					return false;
				} else if (s.charAt(i) == '}' && '{' != parenStk.peek()){
					return false;
				}
				parenStk.pop();
			}
		}
		if (!parenStk.isEmpty()){
			return false;
		}
		return true;
	}

}
