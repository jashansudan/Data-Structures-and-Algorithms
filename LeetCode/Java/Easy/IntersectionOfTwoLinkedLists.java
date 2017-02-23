package Easy;

public class IntersectionOfTwoLinkedLists {

	public static void main(String[] args){
		
	}
	
	
	public ListNode getIntersectionNode(ListNode headA, ListNode headB){
		int lenA = getLength(headA);
		int lenB = getLength(headB);
		
		if (lenA > lenB){
			int diff = lenA-lenB;
			while (diff > 0){
				headA = headA.next;
				diff--;
			}
		}
		if (lenB > lenA){
			int diff = lenB-lenA;
			while (diff > 0){
				headB = headA.next;
				diff--;
			}
		}
		
		while (headA!= null && headB != null){
			if (headA == headB){
				return headA;
			}
			headA = headA.next;
			headB = headB.next;
		}
		return null;
	}
	
	
	public int getLength(ListNode head){
		int count = 0;
		
		while (head != null){
			count++;
			head = head.next;
		}
		
		return count;
	}
	
}
