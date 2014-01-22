import java.util.*;
public class run {
    public static void main(String[] args) {
	Scanner s = new Scanner(System.in);
	int l = s.nextInt();
	int[] arr = new int[l];
	int count = 0;
	for(int i = 2; i < arr.length; i++) {
	    for(int j = i; j < arr.length; j += i) {
		arr[j]++;
	    }
	    if(arr[i] == 2) {
		count++;
	    }
	}
	System.out.println(count);
    }
}