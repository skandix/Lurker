import os

from dotenv import load_dotenv


class Settings:
    def __init__(self):
        self.ROOT_DIR = os.environ.get("ROOT_DIR")