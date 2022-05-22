from loguru  import logger as log
from pathlib import Path

from .settings import Settings

class Lurker:
    def __init__(self):
        self.DOT = Settings()

    def wat(self):
        print ("wat")