# Asymmetric cryptography
print('ASYMMETRIC CRYPTOGRAPHY:')
p = 11
q = 17
n = p * q
print('\nComposite number is:', n)

rp = (p-1) * (q-1)
print('\n(p-1) * (q-1)=', rp)

e = 7

message = 'A'
print('\nMessage prior encryption:', message)
ASCII_eq = ord(message)
print('ASCII equivalent of message:', ASCII_eq)

encrypted_message = ASCII_eq ** e % n
print('\nEncrypted message is:', encrypted_message)

# Hashing
print('\nHASHING: ')

import hashlib
message_not_hashed = 'hello'
print('Message:', message_not_hashed)
hashed_message = hashlib.sha256(b'hello').hexdigest()
print('Hashed message:', hashed_message)
print('Length of hash:', len(hashed_message))

