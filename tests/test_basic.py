"""Basic tests for sanity checking."""


import os
import buckler


def test_password_creation():
    """Make sure passwords are being generated in the right ways."""
    length = 16
    passwd = buckler.encrypt.create_passwd(length)
    assert len(passwd) == length


def test_password_encrypt_decrypt(tmpdir):
    """Test that we can decrypt and encrypt a password."""
    passwd = b"hello"
    key = b"world"
    file = os.path.join(tmpdir, "test_password")
    buckler.encrypt.save_to_file(file, key, passwd)
    result = buckler.encrypt.read_from_file(file, key)
    assert result == passwd


def test_encrypt_decrypt_wrappers(tmpdir):
    """Test the higher level integrate functions for reading and writing."""
    key = b"new key"
    passwd = buckler.create_password(key, "google", length=24,
                                     directory=tmpdir, memory=1024,
                                     mixing=1)
    assert (buckler.read_password(key, "google", directory=tmpdir)
            == passwd)
