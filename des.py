import base32hex
import hashlib
from Crypto.Cipher import DES
key = 'password'
m = hashlib.md5(key)
key = m.digest()
(dk, iv) =(key[:8], key[8:])
crypter = DES.new(dk, DES.MODE_CBC, iv)

plain_text= "I see you"

print("The plain text is : ",plain_text)
plain_text += '\x00' * (8 - len(plain_text) % 8)
ciphertext = crypter.encrypt(plain_text)
encode_string= base32hex.b32encode(ciphertext)
print("The encoded string is : ",encode_string)
