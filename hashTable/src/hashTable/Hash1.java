package hashTable;
import java.util.*;
public class Hash1 {

	public static void main(String Args[]) {
	Hashtable<String,Double> h1= new Hashtable();
	
	h1.put("name1", 3456.56);
	h1.put("name2", 456.56);
	h1.put("name3", 56.56);
	h1.put("name4", 6.56);
	System.out.println(h1);
    System.out.println(h1.values())	;
    System.out.println(h1.size());
    System.out.println(h1.remove("name2"));
    Set s = h1.entrySet();
    Enumeration e = h1.elements();
    while(e.hasMoreElements()) {
    	System.out.println(e.nextElement());
    }
	}
	
}
