package hashTable;
//
//public class uniqchars {
//	public static void main(String Args[]) {
//		String s= "gdsh mnbb";
//		boolean flag=true;
//		for (int i =0;i<s.length();i++) {
//		  for(int j=0;j<s.length();j++) {
//			  if(s.charAt(i)==s.charAt(j) && i!=j) {
//				 flag = false; 
//				 break;  
//			  }   
//		  }
//		      if(flag==false) {
//		    	  break;
//		      }
//		}
//		if(flag!=true) {
//			  System.out.println(" not uniq");
//		  }
//		else {
//			System.out.println(" uniq");
//		}
//	}
//}


import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class  uniqchars{
    
    public static void main (String args[])
    {
        boolean result=false;
        String inputstring="Alve i@wsom";
        System.out.println(inputstring);
        HashSet < Character> uniquecharset= new HashSet();
        for(int i=0;i < inputstring.length();i++)
        {
            result=uniquecharset.add(inputstring.charAt(i));
            if (result == false)
            break;
        }
    System.out.println(result); }
}