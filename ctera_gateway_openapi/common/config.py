import os


class Config():
    __instance = None

    @staticmethod
    def instance():
        if Config.__instance is None:
            Config()
        return Config.__instance

    def __init__(self):
        if Config.__instance is not None:
            raise Exception("Vault is a singleton class.")
        self._hostname = os.environ.get('CTERA_FILER_ADDRESS', '127.0.0.1')
        self._username = os.environ.get('CTERA_FILER_USERNAME')
        if self._username is None:
            raise Exception("Environment variable CTERA_FILER_USERNAME is not set")
        self._password = os.environ.get('CTERA_FILER_PASSWORD')
        if self._password is None:
            raise Exception("Environment variable CTERA_FILER_PASSWORD is not set")
        Config.__instance = self

    @property
    def hostname(self):
        return self._hostname

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password
