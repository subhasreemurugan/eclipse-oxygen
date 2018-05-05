package hashTable;
import java.util.*;


public class uniq_hash {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
      String s1 = "fdfj kjk";
      int k,v;
      boolean flag=true;
      Hashtable h= new Hashtable(); 
      for(int i=0;i<s1.length();i++) {
    	  k= (int) (s1.charAt(i));
    	  v=(int)h.get(k)+1;
    	  h.put(k, v);  
      }+      for(int i=65;i<123;i++) {
    	  System.out.println(h.get(i));
    	  if((int)h.get(i)>1) {
    		  flag=false;
    		  System.out.println("not uniq");
    		  break;
    	  }
      }
      if(flag==true) {
    	  System.out.println("uniqe");
      }
 	}

}
