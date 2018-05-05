package hashTable;

public class replace {
	public static void main(String Args[]) {
	String str= "wat the ";
	char[] str_arr=str.toCharArray();
	
	int count=0;
	for (int i = 0;i<str_arr.length;i++) {
		if(str_arr[i]==' ') {
			count++;
			
		}
		
	}
	int len=count*2+str_arr.length;
	char[] arr1= new char[len];
	System.out.println(len +"" +count);
	
	for (int i = str_arr.length-1;i>=0;i--) {
		//System.out.println("ii"+str_arr[i]+len+" "+i+" "+str_arr[i]);
		if(str_arr[i]==' ') {
			
			arr1[len-1]='%';
			arr1[len-2]='0';
			arr1[len-3]='2';
			len=len-3;
			
			//System.out.println("len"+""+str_arr[6]);
		}
		else {
			System.out.println("len"+""+len);
			//System.out.println("len"+""+str_arr[6]);
			arr1[len-1]=str_arr[i];
			
			len=len-1;
		}
		
	}
	System.out.println(arr1);
	}
	
}
