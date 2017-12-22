
import java.util.Scanner;

public class Decryption {

	
	
	public static void main(String []args) {
		
		String alphabet = "abcdefghijklmnopqrstuvwxyz";
		
		System.out.println("Enter Encrypted Text: ");
		Scanner reader = new Scanner(System.in);  // Reading from System.in
		String encryptedText = reader.next();
		System.out.println("startKey" + " " + "=" + " " + " " + encryptedText);
		
		System.out.println("Enter the startKey: ");
		Scanner reader2 = new Scanner(System.in);  // Reading from System.in
		String startKey = reader2.next();
		System.out.println("startKey" + " " + "=" + " " + " " + startKey);
		
		String key = startKey + alphabet;
		
		for(int i = 0; i < startKey.length(); i++) {
			
			char letter = encryptedText.charAt(i); // something with this line with long startkeys?
			int alphabetPos = alphabet.indexOf(letter);
			char encryptedLetter = key.charAt(alphabetPos);
			System.out.print(encryptedLetter);
			// just outputs startkey
			
		}
		
	}
}
