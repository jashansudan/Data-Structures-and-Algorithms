package Easy;

public class RemoveLinkedListElement {

	public static void main(String[] args) {


	}
	
	public ListNode removeElements(ListNode head, int val){
		if (head == null){
			return head;
		}
		while (head.val == val){
			head = head.next;
			if (head == null){
				return head;
			}
		}
		ListNode ptr = head;
		while (ptr != null){
			if(ptr.val == val){
				ptr.val = ptr.next.val;
				ptr.next = ptr.next.next;
			}
			else {
				ptr = ptr.next;
			}
		}
		return head;
	}

}
