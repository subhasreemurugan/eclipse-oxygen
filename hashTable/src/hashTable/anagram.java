package hashTable;

import java.util.Arrays;

public class anagram {
	public static void main(String args[]) {
		String str = "geeks";
		String str1 = "keegxcvcds";
		//String s = new String();
		char[] c= str.toCharArray();
		char[] b= str1.toCharArray();
		Arrays.sort(c);
		Arrays.sort(b);
		String a = new String(c);
		System.out.println(c);
		System.out.println(b);
		//System.out.println(Arrays.toString(c));
		System.out.println(anaeq(c,b));
	
	}
	public static boolean  anaeq(char[] c, char[] b) {
	boolean r=Arrays.equals(c, b);
	return r;
	}
}
 