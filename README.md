Buckler - Python Powered Password Protector
=======

A simple command line password manager, using Scrypt and written in pure python

NOTE: The implementation of Scrypt used in this project is PURE Python, and fairly slow.

## Getting Started

Install buckler from this repository:
```
git clone https://github.com/madelyneriksen/buckler
cd buckler
virtualenv -p python3 .env  # Or whichever virtual environment
source .env/bin/activate
python setup.py install
```

Basic usage:
```
buckler create myspace  # Create a password
buckler create gmail
buckler get myspace  # Get a password from the filesystem
buckler show  # Show all passwords
buckler rotate  # Change key used for encryption
```

### License

Buckler is made avaliable under the MIT License.
