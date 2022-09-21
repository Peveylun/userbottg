from os import environ
from typing import Final


class TgKeys:
    API_ID: Final = environ.get('API_ID', 'define me!')
    API_HASH: Final = environ.get('API_HASH', 'define me!')
