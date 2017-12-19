public class LRUCache {

	int capacity;
	listNode head;
	listNode tail;
	HashMap<Integer, listNode> numMap = new HashMap<>();

	public LRUCache(int c){
		this.capacity = c;
		head = new listNode(0, 0);
		tail = new listNode(0, 0);
		head.next = tail;
	}

	public int get(int key){
		if (numMap.containsKey(key)){
			listNode temp = numMap.get(key);
			delete(temp);
			insertFront(temp);
			return temp.val;
		}
		else {
			return -1;
		}
	}

	public void put(int key, int val){
		listNode newNode = new listNode(key, val);
		if (numMap.size() == capacity){
			numMap.remove(tail.prev.val);
			delete(tail.prev);
		}
		insertFront(newNode);
		numMap.put(key, newNode);
	}

	public void insertFront(listNode node){
		node.next = head.next;
		node.prev = head;
		node.next.prev = node;
		head.next = node;
	}

	public void delete(listNode node){
		node.next.prev = node.prev;
		node.prev.next = node.next;
	}

}

class listNode{
	public int key;
	public int val;
	public listNode prev;
	public listNode next;

	public listNode(int k, int v){
		this.key = k;
		this.val = v;
	}

}