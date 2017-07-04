package Easy;

import java.util.*;

public class PalindromeLinkedList {

	public static void main(String[] args) {

	}
	
	public boolean isPalindrome(ListNode head){
		int len = 0;
		ListNode ptr = head;
		while (ptr != null){
			ptr = ptr.next;
			len++;
		}
		ptr = head;
		
		Stack<Integer> stk = new Stack();
		int count = 0;
		while(len/2 > count){
			stk.push(ptr.val);
			ptr = ptr.next;
			count++;
		}
		if (len %2 == 1) ptr = ptr.next;
		
		while (ptr != null){
			if (stk.pop() != ptr.val) return false;
			ptr = ptr.next;
		}
		return true;
	}
	


}
