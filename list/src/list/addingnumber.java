package list;

public class addingnumber {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		listmethod l1= new listmethod();
		listmethod l2 =new listmethod();
		l1.addele(3);
		l1.addele(1);
		l1.addele(5);
		l2.addele(5);
		l2.addele(9);
		l2.addele(2);
		l1.show();
		l2.show();
		listmethod l3;
		l3= l1.addlist(l2);
		System.out.print("the sum of the list =");
		l3.show();

	}

}