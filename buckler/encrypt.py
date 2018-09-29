"""Module for handling the encryption of files with Scrypt"""

import pyscrypt


def save_to_file(filename: str, key: bytes, contents: bytes,
                 N=1024, r=1, p=1):
    """Use scrypt to write and save an encrypted file.

    Arguments:
        filename: Name of the file to write to.
        key: The key to use for encryption.
        contents: The contents of the encrypted file.
        N: From Scrypt, the general work factor.
        r: From Scrypt, the memory cost.
        p: From Scrypt, the computation cost.
    Returns:
        None.
    """
    with pyscrypt.ScryptFile(filename, key, N, r, p) as file:
        file.write(contents)


def read_from_file(filename: str, key: bytes) -> bytes:
    """Read the contents of a file when given a specific key."""
    with pyscrypt.ScryptFile(filename, key) as file:
        return file.read()
