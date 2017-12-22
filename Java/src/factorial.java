import java.util.Scanner;

public class factorial {
	
	public static void main(String []args) {
		
		System.out.println("Enter a number: ");
		
		Scanner reader = new Scanner(System.in);  // Reading from System.in
		double n = reader.nextDouble();
		double product = n;
		
		for(double i = n; i > 1; i--) {
			
			product = product*(i-1);
			
		}
		
		System.out.println(product);
	}
	
}
