from messageSecurity import messageSecurity

userInput = input('Please enter a word to be encrypted: ')
userPasscode = input('Please enter a passcode to validate encryption and decryption: ')
userKeyPath = input('Please enter the path where your key file is stored (default "keys/key.txt")')
userWantNewKey = input('Would you like to generate a new key to encrypt and decrypt this message? (enter "1" for True or "0" for False): ')

message = messageSecurity(userInput, userPasscode, userKeyPath, userWantNewKey)

print('\nEncrypted Message: ')
print(message.encrypt())

print('\n\nDecrypted Message: ')
print(message.decrypt())