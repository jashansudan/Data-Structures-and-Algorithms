package Easy;

public class SwapNodesInPairs {

	public static void main(String[] args) {

	}
	
	public static ListNode swapPairs(ListNode head){
		ListNode temp = new ListNode(0);
		temp.next = head;
		ListNode ptr = temp;
		
		while (ptr.next != null && ptr.next.next != null){
			ListNode first = ptr.next;
			ListNode second = ptr.next.next;
			first.next = second.next;
			ptr.next = second;
			ptr.next.next = first;
			ptr = ptr.next.next;
		}
		
		return temp.next;
	}

}
