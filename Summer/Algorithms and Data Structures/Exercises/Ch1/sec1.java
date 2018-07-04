public class sec1 {
	
	
	public static void main(String[] args) {
		System.out.println("1.1.1 Give the value of each of the following expressions");
		System.out.println("a. (0 + 15)/2 = " + (0+15)/2 + "\nb. 2.0e-6 * 100000000.1 = " + (2.0e-6*100000000.1) + "\nc. true && false || true && true = " + ((true && false) || (true && true)));
		System.out.println("1.1.2 Give the type and value of each of the following expressions");
		System.out.println("a. (1 + 2.236)/2 = " + (1+2.236)/2 + ", float \nb. 1 + 2 + 3 + 4.0 = " + (1+2+3+4.0) + ", float \nc. 4.1 >= 4 = "+ (4.1 >= 4) + ", boolean \nd. 1 + 2 + \"3\" = "+ (1+2+"3")+ ", string");
		int a = 1;
		int b = 0;
		int c = 1;
		if (a > b) c = 0 else b = 0;
		System.out.println(c);
	}
}
