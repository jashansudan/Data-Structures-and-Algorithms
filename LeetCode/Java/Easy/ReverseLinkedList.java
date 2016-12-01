package Easy;

import java.util.Stack;

public class ReverseLinkedList {

	public static void main(String[] args) {
		
		ListNode test1 = new ListNode(3);
		ListNode test2 = new ListNode(4);
		ListNode test3 = new ListNode(5);
		test1.next  = test2;
		test2.next = test3;
		System.out.println(reverseList(test1).val);

	}
	
	
	public static ListNode reverseList(ListNode head){
		if (head == null){
			return head;
		}
		Stack<Integer> stk = new Stack<Integer>();
		while(head != null){
			stk.push(head.val);
			head = head.next;
		}
		ListNode newHead = new ListNode(stk.pop());
		head = newHead;
		while (!stk.isEmpty()){
			ListNode temp = new ListNode(stk.pop());
			newHead.next = temp;
			newHead = temp;
		}
		return head;
	}

}
