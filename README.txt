2.0:
By: Shane Schroeder
January 15th, 2023

A derivative approach on the Caesar Cipher.

This Repository contains a Python version of my take on 
improving the Caesar Cipher.

My approach is as follows:

    1. Check if a key file exists which is stored in the follwing format:
        {
            encrypted passcode
            shift array
            direction array
        }
    
    2. If a key does not exist at all or the user requested a new key file
    then generate a new one and say it is valid.

    3. If a key does exist, check if it is valid by decrypting from the information in the file.

    4. If it is valid, encryption and decryption may proceed, 
    else return warning strings when trying to do either operation.

To encrypt a string, the string is shifted up or down randomly, a random amount of characters.
The number of characters shifted, and direction of shifting are stored in arrays.

To decrypt a string, read the shift and direction array to shift all the characters back to their
original characters.