package list;

import java.util.HashSet;

public class listmethod {
	node head;
	
	//Add element at the begining
	public void addele(int data) {
	node newnode = new node();
	node n1 = head;
	newnode.data = data;
	newnode.next = null;
	if(head == null) {
		head = newnode;
	}
	else {
		while(n1.next != null) {
			n1 = n1.next;
			
		}
		n1.next = newnode;
	}	
	}
	public void  show() {
		node n1 = head;
		while(n1.next != null) {
			System.out.print(n1.data+", ");
			n1 = n1.next;
		}
		System.out.println(n1.data+".");
	}
	public void delStart() {
		node n1=head;
		head=head.next;
		System.out.println(" this item was deleted start ="+n1.data);
		
	}
	public  void delEnd() {
		
		node n1 = head;
		
		node prev=head;

		while(n1.next != null) {
			//System.out.println(n1.data);
			prev=n1;
			n1 = n1.next;
		}
//      if(n1.next==null) {
//    	head=null;
//    }
//      else {
    	  System.out.println(n1.data+" was deleted at end");
  		  prev.next = null;  
    //  }
		
	}
 public listmethod duplicate(listmethod l1) {
	 listmethod l2= l1;
	// l2.show();
	 node n2= l2.head;
	 node ptr = l2.head;
	 int dupli;
	 while(n2.next != null) {
		ptr= n2;
		while(ptr.next != null) {
			if(n2.data == ptr.next.data) {
				dupli = ptr.data;
				ptr.next = ptr.next.next; 
				System.out.println(dupli);
			}
			else {
				ptr= ptr.next;
			}
		}
		n2=n2.next;
	 }
	 return l2;
	 
	
	 
 }
 public listmethod duplicateHash(listmethod l1) {
	 listmethod l2= l1;
	 l2.show(); 
	 node n1=l2.head;
	 node prev=null;
	 HashSet < Integer> h1 = new HashSet();
	 
	 while(n1 != null) {
		 
		if(h1.contains(n1.data) ) {
			System.out.println(n1.data+" duplicate "+n1.next.next);
		   prev.next = n1.next.next;
		 
		}
		else { 
			h1.add(n1.data);
			prev= n1;
		}
		n1 = n1.next;
	 }
	return l2;
	 
 }
 public listmethod removecenter() {
	 listmethod l2 = this;
	 int count =0;
	 node n1= l2.head;
	 node prev= n1;
	 //l2.show();
	 while(n1 != null) {
		count ++; 
		n1 = n1.next;
	 }
	 int mid= 0;
	 if(count%2==0) {
		 mid=count/2;
	 }
	 else {
		 mid= count/2 +1;
	 }
	 System.out.println(count + " mid = "+ mid);
	 n1=l2.head;
	 for(int i =0;i<mid-1;i++) {
		 prev= n1;
		 n1=n1.next;
		 //System.out.println(n1.data+" - >" +prev.data);
	 }
	 prev.next =n1.next;
	// System.out.println(n1.data+" out - >" +prev.data);
	 
	 return l2;
 }
 public listmethod addlist(listmethod l2) {
	 listmethod l3 = new listmethod();
	 listmethod l1=this;
	 node n1,n2,n3;
	 n1 = l1.head;
	 n2 = l2.head;
	 
	 int carryover,sum;
	 carryover=0;
	 while(n1 != null ) {
		 
	   sum = n1.data + n2.data+ carryover;
	   if(sum>9) {
		   carryover=1;
		   sum=sum%10;
	   }
	   else {
		   carryover = 0;
	   }
	  // System.out.println(" sum "+ n1.data + n2.data+ carryover);
	   l3.addele(sum);
	  // n3.data= sum;
	   //n3.next.data = carryover+sum;
	   n1 = n1.next;
	   n2 = n2.next;
	  
	 }
	 return l3;
 }
 
 public listmethod delnode(int val) {
	 listmethod l2= this;
	 node n1= l2.head;
	 node prev = n1;
	 while(n1 != null) {
		 
		 if(n1.data ==  val) {
			prev.next = n1.next; 
			System.out.println(prev.data+" val "+n1.data);
		 }
		 else {
			 prev = n1; 
		 }
		 n1= n1.next;
	 }
	 return l2;
 }
 public listmethod reverse() {
	 listmethod l1= this;
	 node curr = l1.head;
	 node prev = null;
	 l1.show();
	 node nextnode = curr.next;
	 while (curr != null) {
		 nextnode = curr.next;
		curr.next = prev;
		prev= curr;
		curr = nextnode;
		//nextnode = nextnode.next;
		//System.out.println(prev.data +"curr"+curr.data+"next data"+nextnode.data);
		
		
	 }
	 l1.head=prev;
	
	 return l1;
 }
}
