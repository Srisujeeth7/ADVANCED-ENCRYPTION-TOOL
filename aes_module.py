from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64, os

def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(file_path: str, password: str):
    salt = os.urandom(16)
    key = generate_key(password, salt)
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        data = file.read()

    encrypted = fernet.encrypt(data)
    with open(file_path + '.aes', 'wb') as file:
        file.write(salt + encrypted)

def decrypt_file(file_path: str, password: str):
    with open(file_path, 'rb') as file:
        content = file.read()

    salt, encrypted = content[:16], content[16:]
    key = generate_key(password, salt)
    fernet = Fernet(key)

    decrypted = fernet.decrypt(encrypted)

    original_file = file_path.replace('.aes', '')
    with open(original_file, 'wb') as file:
        file.write(decrypted)
