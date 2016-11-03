import java.util.*;

public class BalancedBrackets {
	
	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++) {
            String expression = in.next();
            boolean answer = isBalanced(expression);
            if(answer)
                System.out.println("YES");
            else System.out.println("NO");
        }
      
    }
	
	public static boolean isBalanced(String expression) {
		char[] charArr = expression.toCharArray();
		Stack<Character> brackets = new Stack<Character>();
		if (charArr.length % 2 != 0 || charArr.length > 100){
			return false;
		}
		for (int i = 0; i < charArr.length; i++){
			if (charArr[i] == '(' || charArr[i] == '[' || charArr[i] == '{' ){
				brackets.push(charArr[i]);
			}
			else {
				if (brackets.empty()){
					return false;
				}
				if (brackets.peek() == '('){
					if (charArr[i] != ')'){
						return false;
					}
				}
				else if (brackets.peek() == '{'){
					if (charArr[i] != '}'){
						return false;
					}
				}
				else {
					if (charArr[i] != ']'){
						return false;
					}
				}
				brackets.pop();
			}
		}
		if (!brackets.empty()){
			return false;
		}
		return true;
    }
	
}
