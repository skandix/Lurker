import io
import json


from loguru import logger as log
from zipfile import ZipFile

from ..settings import Settings


class _Utility:
    def __init__(self):
        self.DOT = Settings()

    def _motd(self):
        return ("feelsshartman")