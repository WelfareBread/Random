import java.util.LinkedList;
import java.util.Scanner;

public class Do_something_fun {
	
	
	
	public static void main(String []args) {
		
		System.out.println("Enter the number of lines you want: ");
		Scanner reader = new Scanner(System.in);  // Reading from System.in
		double n = reader.nextDouble();
		
	
		System.out.println("1");
		System.out.println("1 1");
		
		LinkedList<Integer> currentLine = new LinkedList<>();
		
		currentLine.add(1);
		currentLine.add(1);
		
		double numberOfLines = n;
		
		/*
		1	1
		2	3
		3	5
		4	7
		5	9
		
		6	13
		7	16
		8	19
		9	22
		
		10	27
		*/
		
		for(int j = 0; j < numberOfLines-2; j++) {
			
			LinkedList<Integer> nextLine = new LinkedList<>();
			
			nextLine.add(1);
			
			for(int i = 0; i < currentLine.size()-1; i++) {
				
				int combined = currentLine.get(i) + currentLine.get(i+1);
				nextLine.add(combined);
				
				
			}
			
			nextLine.add(1);
			String final_string = "";
			for(int i = 0; i < nextLine.size(); i++) {
				
				int number = nextLine.get(i);
				String bro = "0";
				bro = bro.valueOf(number);
				
				final_string = final_string + bro + " ";
				
			}
			 
			
			System.out.println(final_string);
			currentLine = nextLine;
			
		}
	
	}
	

}
