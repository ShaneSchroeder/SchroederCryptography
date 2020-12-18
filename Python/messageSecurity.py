import random
class messageSecurity:

    message = ""
    shifts = []
    operations = []
    encryptedMessage = ""

    def __init__ (self, message):
        self.message = message

    def encrypt(self):
        if(self.message == ""):
            return ""
        
        encrypted = ""

        self.shifts = [0 for x in range(len(self.message))]
        self.operations = [0 for x in range(len(self.message))]

        chars = list(self.message)

        for i in range(len(self.message)):
            
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

    def decrypt(self):

        if(self.message == ""):
            return ""

        decrypted = ""

        chars = list(self.encryptedMessage)

        for i in range (len(self.message)):

            if(self.operations[i] == 0):
                chars[i] = chr(ord(chars[i]) - int(self.shifts[i]))

            if(self.operations[i] == 1):
                chars[i] = chr(ord(chars[i]) + int(self.shifts[i]))
            
        decrypted = decrypted.join(chars)

        return decrypted