package Easy;

public class RemoveDuplicatesFromSortedLinkedList {

	public static void main(String[] args) {


	}
	
	public static ListNode deleteDuplicates(ListNode head){
		ListNode ptr = head;
		if (ptr == null){
			return head;
		}
		while(ptr.next != null){
			if (ptr.next.val == ptr.val){
				ptr.next = ptr.next.next;
			}
			else {
				ptr = ptr.next;
			}
		}
		return head;
	}

}
