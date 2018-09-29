"""Library file for buckler"""


import logging
from .integrate import create_password, read_password


logging.getLogger(__name__).addHandler(logging.NullHandler())
