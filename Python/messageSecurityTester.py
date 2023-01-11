from messageSecurity import messageSecurity

userInput = input('Please enter a word to be encrypted: ')
userPasscode = input('Please enter a passcode to validate encryption and decryption: ')
userKeyPath = input('Please enter the path where your key file is stored (default "keys/key.txt")')

message = messageSecurity(userInput, userPasscode, userKeyPath)

print('\nEncrypted Message: ')
print(message.encrypt())

print('\n\nDecrypted Message: ')
print(message.decrypt())