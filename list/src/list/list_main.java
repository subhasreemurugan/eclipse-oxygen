package list;

public class list_main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		listmethod l1= new listmethod();
		listmethod l2;
		l1.addele(10);
		//l1.show();
		l1.addele(11);
		l1.addele(12);
		l1.addele(111);
		l1.addele(121);
		l1.addele(13);
		l1.addele(15);
		l1.show();
		
		l2 = l1.delnode(121);
		l2.show();
		
//		l2 = l1.removecenter();
//		l2.show();
//		
//		l2 = l1.duplicate(l1);
//		System.out.println("list out of duplicate");
//		l2.show();
		
//		l2 = l1.duplicateHash(l1);
//		System.out.println("list out of duplicate Hash");
//		l2.show();
		
		//l1.delStart();
		//l1.show();
//        l1.delEnd();
//        l1.show();
//        l1.delEnd();
//        l1.show();
		
	}

}
