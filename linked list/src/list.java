
public class list {
	node head;
//	list(){
//		 head= null;
//	}
	
	//add  at the end
	void addele(int data) {
		node newNode = new node();
		newNode.data = data;
		newNode.next=null;
		if (head == null) {
			head = newNode;
			
		}
		else {
			node n = head;
			//System.out.println(head.data);
			//System.out.println(n.data+ " "+n.next);
			while(n.next != null) {
			n = n.next;	
			}
			n.next = newNode;
			
		}
	}
	
	//show the all elemnet
	void show() {
		node n = head;	
		while(n.next!=null) {
			System.out.println(n.data);
			n = n.next; 
			
			}
		System.out.println(n.data);
	}
	
	//insert at  the begining
	 public void addstart(int data) {
		 node newNode = new node();
		 newNode.data = data;
		 newNode.next =head;
		 head = newNode;
	 }
	 
	 //delete at the end
//	 public void delend() {
//		 if(head==null) {
//			 System.out.println("nothong to del");
//		 }
//		 else {
//			 node n = head;
//			 node m = n.next;
//			 while(m.next != null) {
//				 n=n.next;
//				 m=n.next;
//				
//			 }
//			 n.next=null;  
//			 System.out.println(m.data +"deleted");
//		 }
//		
//	 }
	 
	 // to insert at a position
	 public void addPos(int posi,int data) {
		 
		 //tmp =newNode only
		 node tmp = head;
		 node newNode = new node();
		 newNode.data = data;
		 int counter = 0;
		 if(posi == 0)
		 {
			 addstart(data);
		 }
		 else {
			 while( posi !=counter) {
					counter++;
					tmp = tmp.next;
				 }
				 
				 newNode.next = tmp.next;
				 tmp.next = newNode; 
		 }
		 
		 
	 }
	 
	 //del at pos
	 public void delPos(int posi) {
		 int counter = 0;
		 if(posi == 0) {
			head = head.next; 
		 }
		 else {
			 node tmp = head;
			 node prev = null;
			 while(posi != counter) {
				 counter ++;
				prev = tmp;
				tmp = tmp.next; 
				
			 }
			 System.out.println("deleted" +tmp.data);
			 prev.next=tmp.next;
			 
		 }
		
		 	 
	 }
	}
