"""
Copyright 2023 Shane Schroeder

A simple encryption and decryption program for plain text.
It is basically a more sophisticated Caesar Cipher that 
relies on random numbers for the amount and direction to 
shift characters.

Will use generate something like an ssh key to validate encryption
and decryption based on a passcode.
"""
import random
import json
import pathlib
class messageSecurity:

    message = ""
    passcode = ""
    shifts = []
    operations = []
    encryptedMessage = ""
    pathToKeyFile = ""
    hasValidKey = False

    def __init__ (self, message, passcode, pathToKeyFile, generateNewKey=0):
        self.message = message
        self.passcode = passcode
        if pathToKeyFile == "":
            self.pathToKeyFile = 'keys/key.txt'
        else:
            self.pathToKeyFile = pathToKeyFile

        # check if the path to the key exists
        if pathlib.Path(self.pathToKeyFile):
            keyExists = True
        
        # if the key does not exist, create key
        if not keyExists or generateNewKey == 1:
            print("Generating new key...")
            self.generateKeyFile()
            print("New key created at: {0}".format(self.pathToKeyFile))
        # check for validity
        self.hasValidKey = self.checkKeyFile()
        
        # Will now use the variable to allow encryption/decryption, 
        # if not valid, return warning strings from both ^, else allow it.

    def checkKeyFile(self):
        """
        Will check if the existing key file matches the entered password to encrypt/decrypt
        """
        try:
            encryptedPasscode = ""
            shiftsForPasscode = ""
            operationsForPasscode = ""
            key = open(self.pathToKeyFile, 'r')
            if len(key.readlines()) != 3:
                return False
            key.seek(0)
            encryptedPasscode = key.readline().strip()
            shiftsForPasscode = json.loads(key.readline().strip())
            operationsForPasscode = json.loads(key.readline().strip())
            key.close()
            self.hasValidKey = True
            decryptedPass = self.decrypt(encryptedPasscode, shiftsForPasscode, operationsForPasscode)
            self.hasValidKey = False
            if decryptedPass == self.passcode:
                return True
            return False
        except IOError:
            return False

    def generateKeyFile(self):
        """
        Will generate a new key file stored in the following format

        {encrypted passcode}
        {shift array}
        {direction array}

        """
        self.hasValidKey = True
        with open(self.pathToKeyFile, 'w') as key:
            key.write(self.encrypt(self.passcode)+'\n')
            key.write(str(self.shifts) + '\n')
            key.write(str(self.operations)+'\n')
            key.close()
            self.shifts = []
            self.operations = []
    
    def encrypt(self, stringToEncrypt=None):
        """
        This method will encrypt a plain text message. It will do so by basically either 
        shifting up or down randomly a character from unicode numbers.
        This method will also handle the *annoying* smart quote from Microsoft's programs.
        """

        if not self.hasValidKey:
            return "No valid key to encrypt"

        if(stringToEncrypt == None):
            stringToEncrypt = self.message
        if(stringToEncrypt == ""):
            return ""
        
        encrypted = ""

        self.shifts = [0 for x in range(len(stringToEncrypt))]
        self.operations = [0 for x in range(len(stringToEncrypt))]

        chars = list(stringToEncrypt)

        for i in range(len(stringToEncrypt)):
            
            operation = random.randint(0, 1)
            shift = random.randint(0, 127)

            if(operation == 0):
                
                if(chars[i] == '’'):

                    chars[i] = chr(chars[i] - 8178)

                    while(ord(chars[i]) + shift > 126):
                        shift = random.randint(0, 127)

                    self.shifts[i] = shift
                    self.operations[i] = operation
                    chars[i] = chr(ord(chars[i]) + shift)

                else:

                    while(ord(chars[i]) + shift > 126):
                            shift = random.randint(0, 127)

                    self.shifts[i] = shift
                    self.operations[i] = operation
                    chars[i] = chr(ord(chars[i]) + shift)

            if(operation == 1):

                if(chars[i] == ' '):

                    while(ord(chars[i]) + shift > 126):
                            shift = random.randint(0, 127)

                    self.shifts[i] = shift
                    operation = 0
                    self.operations[i] = operation
                    chars[i] = chr(ord(chars[i]) + shift)
                
                else:

                    while(ord(chars[i]) - shift < 32):
                            shift = random.randint(0, 127)

                    self.shifts[i] = shift
                    self.operations[i] = operation
                    chars[i] = chr(ord(chars[i]) - shift)

        encrypted = encrypted.join(chars)

        self.encryptedMessage = encrypted

        return encrypted

    def decrypt(self, stringToDecrypt=None, shifts=None, operations=None):
        """
        Simple decrypt method that will read the lists shift amounts and direction.
        """

        if not self.hasValidKey:
            return "No valid key to decrypt"

        if(shifts == None):
            shifts = self.shifts
        if(operations == None):
            operations = self.operations
        if(stringToDecrypt == None):
            stringToDecrypt = self.encryptedMessage
        if(stringToDecrypt == ""):
            return ""

        decrypted = ""

        chars = list(stringToDecrypt)

        for i in range (len(stringToDecrypt)):

            if(operations[i] == 0):
                chars[i] = chr(ord(chars[i]) - int(shifts[i]))

            if(operations[i] == 1):
                chars[i] = chr(ord(chars[i]) + int(shifts[i]))
            
        decrypted = decrypted.join(chars)

        return decrypted