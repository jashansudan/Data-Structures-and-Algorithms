package Easy;

public class RemoveNthNodeFromEndOfList {

	public static void main(String[] args) {
		

	}
	
	public static ListNode removeNthFromEnd(ListNode head, int n){
		if (head == null){
			return head;
		}
		ListNode fast = head;
		ListNode slow = head;
		while (n > 0){
			fast = fast.next;
			n--;
		}
		if (fast == null){
			head = head.next;
			return head;
		}
		while(fast.next != null){
			fast = fast.next;
			slow = slow.next;
		}
		slow.next = slow.next.next;
		
		return head;
	}

}
