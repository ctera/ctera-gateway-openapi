from cterasdk.object.Gateway import Gateway

from ctera_gateway_openapi.common.config import Config


class BaseManager():
    def __init__(self):
        self._gateway = Gateway(Config.instance().hostname)
        self._gateway.login(Config.instance().username, Config.instance().password)
