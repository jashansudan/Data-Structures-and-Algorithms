package Easy;

import java.util.*;

public class ImplementQueuesUsingStacks {
	
	Stack<Integer> stk1 = new Stack();
	Stack<Integer> stk2 = new Stack();

	public void main(String[] args) {
		

	}
	
	
	public void push (int x){
		stk1.push(x);
	}
	
	public void pop(){
		peek();
		stk2.pop();
		
	}
	
	public int peek() {
		if (stk2.empty()){
			while(!stk1.empty()){
				stk2.push(stk1.pop());
			}
		}
		return stk2.peek();
	}
	
	
	public boolean empty() {
		return stk1.isEmpty() && stk2.isEmpty();
	}

}
