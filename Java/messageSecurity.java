/**
 * The messageSecurity class is meant to encapsulate a message into an object. 
 * The class has two methods, encrypt and decrypt. 
 * 
 * Encrypt will shift each character of the message randomly up or down, and by a random amount.
 * It will save what operation was done and how much it was shifted by in private arrays.
 * 
 * Decrypt will undo the encryption by shifting the characters in the correct direction and by the correct amount
 * by referencing the arrays.
 * 
 * @author Shane Schroeder
 * @version 1.0
 * @since 2020-12-18
 *
 */
public class messageSecurity {

	//instance variables
	private String message;
	private int[] shifts;
	private int[] operations;
	private String encryptedMessage = "";

	/**
	 * Empty Constructor. Will assign the message variable to an empty string.
	 */
	messageSecurity(){
		this.message = "";
	}

	/**
	 * Workhorse constructor. Will assign the message variable to whatever string was given.
	 * @param message: String containing what the message is.
	 */
	messageSecurity(String message){
		this.message = message;
	}

	/**
	 * Will shift each character of the message randomly up or down, and by a random amount.
	 * It will save what operation was done and how much it was shifted by in private integer arrays.
	 * 
	 * @return encrypted: String containing the encrypted message.
	 */
	public String encrypt(){

		//if message is empty, returns empty string.
		if(this.message.equals("")) {
			return "";
		}

		//String to contain the encrypted message
		String encrypted = "";
		
		//assigning the integer arrays with size of the length of the message
		this.shifts = new int[ this.message.length() ];
		this.operations = new int[ this.message.length() ];
		
		//character array so the message can be manipulated more easily.
		char[] chars = this.message.toCharArray();
		
		//for each character in the array...
		for(int i = 0; i < this.message.length(); i++) {
			
			/* random integer, either 0 or 1
			 * 0 is for shifting the character up
			 * 1 is for shifting the character down
			 * 
			 * may add more operations like exponentially moving up or down
			 */
			int operation = (int) (Math.random() * 2);

			/* random integer from 0, 127
			 * for storing a random ascii table value.
			 */
			int shift = (int) (Math.random() * 128);
			
			//shifting character up...
			if(operation == 0) {
				
				/*
				 * This character is an exception in the ASCII table that for some reason has a value of 8217.
				 * Needs to be considered explicitly otherwise issues occur.
				 */
				if(chars[i] == '’') {
					
					//readjusts the apostrophe to the one on the standard ASCII table.
					chars[i] = (char) (chars[i] - 8178);
					
					//makes sure the shift does not push the value off the ASCII table.
					while(chars[i] + shift > 126) {
						shift = (int) (Math.random() * 128);
					}

					//adding the amount shifted by to the integer array
					this.shifts[i] = shift;
					
					//adding operation number to the integer array
					this.operations[i] = operation;
					
					//shifting the character up by a random amount
					chars[i] = (char) (chars[i] + shift);

				}
				
				//all other characters other than ’
				else {
					
					//makes sure the shift does not push the value off the ASCII table.
					while(chars[i] + shift > 126) {
						shift = (int) (Math.random() * 128);
					}

					//adding the amount shifted by to the integer array
					this.shifts[i] = shift;
					
					//adding operation number to the integer array
					this.operations[i] = operation;
					
					//shifting the character up by a random amount
					chars[i] = (char) (chars[i] + shift);
					
				}

			}
			
			//shifting character down...
			if(operation == 1) {
				
				/*
				 * With the limits set on which ASCII values I want to use, space is unable to be shifted down without still being a space.
				 * I did not want to clearly give where the spaces were so I instead made it shift up if it tried to shift a space down.
				 */
				if(chars[i] == ' ') {
					
					//makes sure the shift does not push the value off the ASCII table.
					while(chars[i] + shift > 126) {
						shift = (int) (Math.random() * 128);
					}

					//adding the amount shifted by to the integer array
					this.shifts[i] = shift;
					
					//correcting which operation was actually performed
					operation = 0;
					
					//adding operation number to the integer array
					this.operations[i] = operation;
					
					//shifting the character up by a random amount
					chars[i] = (char) (chars[i] + shift);
				}
				
				//all other characters other than space
				else {
					
					//makes sure the shift does not push the value off the ASCII table.
					while(chars[i] - shift < 32) {
						shift = (int) (Math.random() * 128);
					}

					//adding the amount shifted by to the integer array
					this.shifts[i] = shift;
					
					//adding operation number to the integer array
					this.operations[i] = operation;
					
					//shifting the character down by a random amount
					chars[i] = (char) (chars[i] - shift);

				}

			}

		}

		//converting the character array into a string and assigning that string to encrypted
		encrypted = String.valueOf(chars);

		//assigning the class variable to encrypted
		this.encryptedMessage = encrypted;

		//returns the encrypted string
		return encrypted;

	}

	/**
	 * Will undo the encryption by shifting the characters in the correct direction and by the correct amount
	 * by referencing the arrays.
	 * 
	 * @return decrypted: String containing the decrypted message, or in other words, the original message.
	 */
	public String decrypt() {

		//if message is empty, returns empty string.
		if(this.message.equals("")) {
			return "";
		}
		
		//String to contain the decrypted message
		String decrypted = "";
		
		//turning the encrypted message into a character array to more easily be manipulated
		char[] chars = this.encryptedMessage.toCharArray();

		//for each character in the array...
		for(int i = 0; i < this.message.length(); i++) {
			
			//if the operation was to shift up...
			if(this.operations[i] == 0) {
				//shift down by the same amount it was shifted up by
				chars[i] -= shifts[i];
			}

			//if the operation was to shift down
			if(this.operations[i] == 1) {
				//shift up by the same amount it was shifted down by
				chars[i] += shifts[i];
			}

		}

		//converting the character array into a string and assigning that string to decrypted
		decrypted = String.valueOf(chars);
		
		//returning the decrypted string
		return decrypted;

	}


}
