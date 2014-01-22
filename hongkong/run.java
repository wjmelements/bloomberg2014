import java.util.*;
public class run {
    public static void main(String[] args) {
	Scanner s = new Scanner(System.in);
	double total = s.nextDouble();
	int five,three,fifty,twenty,fivec;
	five = three = fifty = twenty = fivec = 0;
	while(total >= 0.001) {
	    if(total - 5.0 >= 0.001) {
		total -= 5.0; five++;
	    } else if(total - 3.0 >= 0.001) {
		total -= 3.0; three++;
	    } else if(total - 0.5 >= 0.001) {
		total -= 0.5; fifty++;
	    } else if(total - 0.2 >= 0.001) {
		total -= 0.2; twenty++;
	    } else {
		total -= 0.05; fivec++;
	    }
	}
	System.out.printf("%d/%d/%d/%d/%d\n",
			  five, three, fifty, twenty, fivec);
    }
}