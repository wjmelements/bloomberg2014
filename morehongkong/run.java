import java.util.*;
public class run {

    public static void main(String[] args) {
	Scanner s = new Scanner(System.in);
	int total = (int)(s.nextDouble()*100.0);
	total = (total + 2) - (total+2)%5;
	System.out.println(num(total,500));
    }

    public static int num(int total, int step) {
	if(total < 0)
	    return 0;
	int ret = 0;
	if(total == 0)
	    return 1;
	if(step == 5) {
	    ret = 1;
	}
	if(step == 20) {
	    ret = num(total-20, step) + num(total, 5);
	}
	if(step == 50) {
	    ret = num(total-50, step) + num(total, 20);
	}
	if(step == 300) {
	    ret = num(total-300, step) + num(total, 50);
	}
	if(step == 500) {
	    ret = num(total-500, step) + num(total, 300);
	}
	return ret;
    }
}