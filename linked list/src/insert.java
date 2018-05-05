
public class insert {
public static void main(String args[]) {
	list l1= new list();
	l1.addele(50);
	l1.addele(25);
	l1.addstart(1);
	l1.addstart(2);
	l1.show();
	//System.out.println(l1);
//	l1.delend();
//	l1.show();
//	
//	l1.delend();
//	l1.show();
//	
//	l1.delend();
//	l1.show();
//	
//	l1.delend();
//	l1.show();
//	
	l1.addPos(2, 99);
	l1.show();
	System.out.println("insert T the begin");
	l1.addPos(0, 0);
	l1.show();
	System.out.println("delete T the begin");
	l1.delPos(0);
	l1.show();
	System.out.println("delete aT the 3");
	l1.delPos(3);
	l1.show();
	
}
}
