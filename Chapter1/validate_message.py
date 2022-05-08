# validate_message.py

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def fetch_public_key(user):
    with open(user.decode('ascii') + "key.pub", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
           key_file.read(),
           backend=default_backend())
    return public_key

# Message coming from user
message = b"Nelson likes cat"

# Signature coming from user
signature = b'!\xf3\x0c\x1d?Qv\xa2ic\xd5\x06\xc7\xa6}eR\xd5\xae\xc0*l9\xfe\x0f\xc7\x02\x0e7\xe3\x02\xcbv\xce\r\xb1.\xc93\x14b\xff\xe3c\xfa%7t\xf1\xb1\xe4\x02\xd83\xc6\xfes\xd1\xb0\xff\xc4\x8b\xabX\x1f\xfdZ;\x15\x90\x8b\xc50\x8d@\xacW\x90\xaf\xd3*n1\x8f\x8a\xafK\xae\xd0C\xf0%1\xeb\x95\xdcbQK\x10\xba\x84\xda\xd8\x1f\xe6N\xd1O\xf2\x99\xa2\x89BNe\xee\x92<\x06\xce\x98\x92\x80\x11\x9e\xe8O'

user = message.split()[0].lower()
# fetch public key from Nelson
public_key = fetch_public_key(user)
# … verify the message like before
public_key.verify(
    signature,
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256())
