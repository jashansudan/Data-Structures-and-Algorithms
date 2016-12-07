package Easy;

public class LinkedListCycle {
	
	public static void main (String[] args){
		
	}
	
	public static boolean hasCycle(ListNode head){
		if (head == null){
			return false;
		}
		ListNode ptrSlow = head;
		ListNode ptrFast = head.next;
		while(ptrFast != null && ptrFast.next != null){
			if (ptrSlow == ptrFast){
				return true;
			}
			ptrSlow = ptrSlow.next;
			ptrFast = ptrFast.next.next;
		}
		
		return false;
	}
}
