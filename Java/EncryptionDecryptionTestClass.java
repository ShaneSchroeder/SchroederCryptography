import java.util.Scanner;

public class EncryptionDecryptionTestClass {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		
		System.out.println("Please enter a word to be encrypted");
		String user = in.nextLine();
		
		messageSecurity message = new messageSecurity(user);
		
		System.out.println();
		
		System.out.println("Encrypted Message: ");
		
		String encrypted = message.encrypt();
		
		System.out.println(encrypted);
		
		System.out.println();
		System.out.println();
		
		
		System.out.println("Decrypted Message: ");
		
		String decrypted = message.decrypt();
		
		System.out.println(decrypted);
		
		System.out.println();
		
		in.close();
	}

}
