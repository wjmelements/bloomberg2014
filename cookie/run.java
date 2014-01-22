import java.util.*;
public class run {
    public static void main(String[] args) {
	Scanner s = new Scanner(System.in);
	int w = s.nextInt();
	int h = s.nextInt();
	System.out.printf("%.3f\n", leftovers(w, h));
    }

    public static double leftovers(double w, double h) {
	while(true) {
	    int numw = (int)Math.floor(w/4.0);
	    int numh = (int)Math.floor(h/4.0);
	    int num = numw*numh;
	    if(num <= 0) {
		return w*h;
	    }
	    double area = w*h - num*Math.PI*4;
	    double nh = Math.sqrt(area*h/w);
	    double nw = Math.sqrt(area*w/h);
	    w = nw; h = nh;
	    //System.out.println("(" + num + "," + w + "," + h + ")");
	}
    }
}