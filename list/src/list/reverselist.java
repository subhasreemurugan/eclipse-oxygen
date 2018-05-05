package list;

public class reverselist {
	public static void main(String args[]) {
	    listmethod l1= new listmethod();
	    listmethod l2;
	    l1.addele(10);
		l1.addele(11);
		l1.addele(12);
		l1.addele(111);
		l1.addele(121);
		l1.addele(13);
		l1.addele(15);
	    l2= l1.reverse();
	    l2.show();
	    
	}

}
