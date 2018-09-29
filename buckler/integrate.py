"""Glue for the different functions.

Connets the user's clipboard, manages passwords, and generally connects
otherwise independent parts of buckler.
"""


import os
import pyscrypt
from buckler import encrypt


BUCKLER_DIR = os.path.join(os.path.expanduser("~"), ".buckler/")


def check_token(key: bytes, directory=BUCKLER_DIR) -> bool:
    """Check the stored TOKEN_FILE, creating it if it doesn't exist.

    The token is then used for verifying the given key, checking it against
    the scrypt checksum.

    Arguments:
        key: The user's key or "password".
    Returns:
        result: True for the key is valid or created, false otherwise.
    """
    os.makedirs(directory, exist_ok=True)
    token = os.path.join(directory, ".token")
    if os.path.exists(token):
        try:
            encrypt.read_from_file(token, key)
            result = True
        except pyscrypt.InvalidScryptFileFormat:
            result = False
    else:
        token_contents = encrypt.create_passwd(length=64)
        encrypt.save_to_file(token, key, token_contents)
        result = True
    return result


def create_password(key: bytes, name: str, length=24,
                    directory=BUCKLER_DIR) -> str:
    """Create a password, save it, and return it as a string.

    We return the password rather than force the user to decrypt it, so that
    upon creation the user can easily paste the password into a sign up form.

    Arguments:
        key: The key used to encrypt the password.
        name: Name of the password (ex. gmail)
        length: Length of the password.
        directory: The directory where the password is saved.
    Returns:
        passwd: A randomly generated password.
    """
    if not check_token(key, directory):
        raise ValueError("Provided key does not match stored token.")
    passwd = encrypt.create_passwd(length)
    passwd_file = os.path.join(directory, name)
    encrypt.save_to_file(passwd_file, key, passwd)
    return passwd.decode()


def read_password(key: bytes, name: str, directory=BUCKLER_DIR) -> str:
    """Read a password that's stored.

    Arguments:
        key: Key used for encrypting the password originally.
        name: The filename of the password.
        directory: Directory where passwords are stored.
    Returns:
        passwd: Decrypted, stored password.
    """
    if not check_token(key, directory):
        raise ValueError("Provided key does not match stored token.")
    passwd_file = os.path.join(directory, name)
    if not os.path.exists(passwd_file):
        raise FileNotFoundError("The requested password does not exist!")
    passwd = encrypt.read_from_file(passwd_file, key)
    return passwd.decode()
