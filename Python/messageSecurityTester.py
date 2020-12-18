import messageSecurity

print('')
print('')

user = input('Please enter a word to be encrypted: ')

message = messageSecurity.messageSecurity(user)

print('')

print('Encrypted Message: ')
print(message.encrypt())

print('')
print('')

print('Decrypted Message: ')
print(message.decrypt())

print('')
print('')